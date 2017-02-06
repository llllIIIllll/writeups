__Bandit :: Level 24__
================

_John Hammond_ | _Friday, November 4th, 2016_ 

> A daemon is listening on port `30002` and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

----------

Log in as usual to the account with the password you retrieved from the previous level.

```
ssh bandit24@bandit.labs.overthewire.org
```

The challenge prompt tells us that there is a [daemon][daemon] (a background service, or program running behind the scenes) that will give us the password for the next level on port `30002`. Let's try and connect to that program with [`netcat`][netcat], like we have done before.

``` 
$ netcat localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
```

Okay, so it tells us that it wants the password and a certain four-digit pincode on one line, just separated by a space. Let's try it, just sending it some test data:

```
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 1234
```

And I get...

```
Wrong! Please enter the correct pincode. Try again.
```

Hmm. I guess `1234` was wrong. Dang! :)

So okay, we know how we can interact with the thing. Let's try and automate the process. We can [pipe] input into the program the same way we [pipe] anything. We can use that [`echo`][echo] command to display [standard output], and [pipe] it to send it as input to the [`netcat`][session].

So first, (if you haven't already) break out of the current connection with `Ctrl+C`.

Then we'll try to [pipe] that same input.

```
$ echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 1234" | netcat localhost 30002
```

Now, after entering that command, we see

```
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct pincode. Try again.
Exiting.
```

... all at once, because we have automated our interaction with it. 

But how can we figure out the correct four-digit pincode that the service wants? Well, the challenge prompt tells us that we need to [brute force] it. This means trying _every single possibility_ until we hit the correct one. We can do that, can't we?

You remember the [`for` loop][for loop] in the last level, right? I said that it could loop over things, like files or indices or even numbers. It can _count_. Couldn't we have it count up and iterate over all of the possible digits, as a four-digit pincode?

First, let's try and test it on the [command-line], just interacting with [`bash`][bash]... then we can formalize it into a  [`bash`][bash] [script], so it is a little cleaner and easier to read and understand. First, let's try and just test the functionality.

As a "one-liner" on just the [`bash`][bash] [command-line], the syntax for the [`for` loop][for loop] is a condition and a sequence of commands separated beginning with a  `do` statement, the commands separated with a `;` semi-colon, and then finally a `done` statement to say that is everything we want to do as part of our loop.

So, just a simple thing to print out numbers 0 through 10...

``` bash
$ for i in {0..10}; do echo "$i"; done
```

Nice, they are all [`echo`][echo]ed out. How can we make it a "four-digit" pincode? Well, we can supply more digits in that list specification. Try this one:

``` bash
$ for i in {0000..0010}; do echo "$i"; done
```

That output should give us a framework for trying a bunch of four-digit possibilities. Now, let's turn it into a script and actually do what we need to do.

First, we should change into a directory that we can work in; some workspace for ourselves. Let's just create a directory in the [temporary directory] to call our own.

```
$ mkdir /tmp/our_workspace
```

... and head there...

```
$ cd /tmp/our_workspace
```

And let's start to write our script.

```
$ nano our_script.sh
```

So in the script, the syntax for the [`for` loop][for loop] can be expanded, and expressed over multiple lines so it looks clean. Rather than just semi-colons, now we can use newlines to denote a different command.

``` bash
#!/bin/bash

for i in {0000..9999}
do
    echo "$i"
done
```

And we can loop through all the needed digits, going from `0000` to `9999`, so we hit all the possible "four-digit pincodes".

Let's make the [script] executable and just see it in action, to verify our [`for` loop][for loop] works as it should:

```
$ chmod +x our_script.sh
$ ./our_script.sh
```

You should see the numbers fly across the screen.

Now, we can change the line inside the [`for` loop][for loop] to try and run the old [piped][pipe] [`netcat`][netcat] command like before ... but we'll replace the static number with our changing variable `$i`!

``` bash
#!/bin/bash

for i in {0000..9999}
do
    echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i" | netcat localhost 30002 
done
```

If you run this code, now, you'll see that it tries to [brute force] all the numbers. However, this ends up creating a new [`netcat`][netcat] session over and over again, one that opens and closes with each iteration. I'm sure you can see, it is pretty slow. So this solution isn't ideal.

But it does work. If you are feeling patient, you can let the thing run for a good couple of hours. You may want to set up some [`grep`][grep] tests to see if you get something other than `Wrong!` each time and can actually determine when the password is displayed.

To save you the time, you should find that the PIN `5669` is the correct PIN.

```
echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 5669" | netcat localhost 30002
```

...

```
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
```


__The password for bandit25 is `uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG`.__


[netcat]: https://en.wikipedia.org/wiki/Netcat
[Wikipedia]: https://www.wikipedia.org/
[Linux]: https://www.linux.com/
[man page]: https://en.wikipedia.org/wiki/Man_page
[man pages]: https://en.wikipedia.org/wiki/Man_page
[man]: https://en.wikipedia.org/wiki/Man_page
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
[port]: https://en.wikipedia.org/wiki/Port_%28computer_networking%29
[ports]: https://en.wikipedia.org/wiki/Port_%28computer_networking%29
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
[redirect]: http://www.tldp.org/LDP/abs/html/io-redirection.html
[pipe]: http://www.tldp.org/LDP/abs/html/io-redirection.html
[piped]: http://www.tldp.org/LDP/abs/html/io-redirection.html
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
[brute-force]: https://en.wikipedia.org/wiki/Brute-force_attack
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
[scripting language]: https://en.wikipedia.org/wiki/Scripting_language
[scripts]: https://en.wikipedia.org/wiki/Scripting_language
[script]: https://en.wikipedia.org/wiki/Scripting_language
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
[automation is divine]: https://www.youtube.com/watch?v=36AA3JGRP9s
[repos]:https://help.ubuntu.com/community/Repositories/Ubuntu
[repo]:https://help.ubuntu.com/community/Repositories/Ubuntu
[repository]:https://help.ubuntu.com/community/Repositories/Ubuntu
[repositories]: https://help.ubuntu.com/community/Repositories/Ubuntu
[hex dump]: https://en.wikipedia.org/wiki/Hex_dump
[hexdump]: https://en.wikipedia.org/wiki/Hex_dump
[xxd]: http://linuxcommand.org/man_pages/xxd1.html
[mkdir]: https://en.wikipedia.org/wiki/Mkdir
[file]: https://en.wikipedia.org/wiki/File_%28command%29
[gzip]: http://www.gzip.org/
[file extension]: https://en.wikipedia.org/wiki/Filename_extension
[bzip]: http://www.bzip.org/
[bzip2]: http://www.bzip.org/
[tar]: https://en.wikipedia.org/wiki/Tar_%28computing%29
[tar command]: http://linuxcommand.org/man_pages/tar1.html
[private key]: https://help.ubuntu.com/community/SSH/OpenSSH/Keys
[s_client]: https://www.openssl.org/docs/manmaster/apps/s_client.html
[nmap]: https://nmap.org/
[IP address]: https://en.wikipedia.org/wiki/IP_address
[RSA]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[ssh private key]: https://help.ubuntu.com/community/SSH/OpenSSH/Keys
[file permissions]: https://www.linux.com/learn/understanding-linux-file-permissions
[octal file permission]: http://www.cyberciti.biz/faq/how-linux-file-permissions-work/
[octal file permissions]: http://www.cyberciti.biz/faq/how-linux-file-permissions-work/
[chmod]: https://en.wikipedia.org/wiki/Chmod
[diff]: http://man7.org/linux/man-pages/man1/diff.1.html
[.bashrc]: http://unix.stackexchange.com/questions/129143/what-is-the-purpose-of-bashrc-and-how-does-it-work
[bashrc]: http://unix.stackexchange.com/questions/129143/what-is-the-purpose-of-bashrc-and-how-does-it-work
[setuid]: https://en.wikipedia.org/wiki/Setuid
[user id]: https://en.wikipedia.org/wiki/User_identifier
[effective user id]: https://en.wikipedia.org/wiki/User_identifier#Effective_user_ID
[cron]: https://en.wikipedia.org/wiki/Cron
[file extension]: https://en.wikipedia.org/wiki/Filename_extension
[file extensions]: https://en.wikipedia.org/wiki/Filename_extension
[bash script]: https://linuxconfig.org/bash-scripting-tutorial
[bash script]: https://linuxconfig.org/bash-scripting-tutorial
[bash scripts]: https://linuxconfig.org/bash-scripting-tutorial
[shebang line]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[she-bang line]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[sha-bang line]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[shabang line]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[sha bang line]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[nano]: https://en.wikipedia.org/wiki/GNU_nano
[text editor]: https://en.wikipedia.org/wiki/Text_editor
[whoami]: https://en.wikipedia.org/wiki/Whoami
[echo]: https://en.wikipedia.org/wiki/Echo_(command)
[md5sum]: http://www.tutorialspoint.com/unix_commands/md5sum.htm
[checksum]: https://en.wikipedia.org/wiki/Checksum
[hash]: https://en.wikipedia.org/wiki/Cryptographic_hash_function
[cut]: https://en.wikipedia.org/wiki/Cut_(Unix)
[daemon]: https://en.wikipedia.org/wiki/Daemon_(computing)
[temporary directory]: https://en.wikipedia.org/wiki/Temporary_folder
[temp directory]: https://en.wikipedia.org/wiki/Temporary_folder
[temp folder]: https://en.wikipedia.org/wiki/Temporary_folder
[temporary folder]: https://en.wikipedia.org/wiki/Temporary_folder
[seq]: http://www.cyberciti.biz/tips/tag/seq-command