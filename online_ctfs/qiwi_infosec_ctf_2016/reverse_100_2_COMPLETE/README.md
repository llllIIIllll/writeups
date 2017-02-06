Reverse 100_2
========

> John Hammond | Monday, November 21st, 2016

--------------------------------------------

> I have a snake. Crack me!

So we are given a [`task.pyc`](task.pyc) file, which is [Python bytecode]. We can decompile this with a lot of tools, the most common being [`uncomplye`][uncompyle] and [Easy Python Decompiler]. During the competition, I used [Easy Python Decompiler]. This created a file for me called [`task.pyc_dis`](task.pyc_dis)

``` python
# Embedded file name: task.py
import marshal
src = 'YwAAAAADAAAAGAAAAEMAAABz7wAAAGQBAGoAAGcAAGQCAGQDAGQEAGQFAGQGAGQHAGQIAGQJAGQKAGQLAGQMAGQNAGQOAGQPAGQMAGcPAERdHAB9AAB0AQB0AgB8AACDAQBkEAAXgwEAXgIAcToAgwEAfQEAdAMAZBEAgwEAfQIAfAIAfAEAawIAcuYAZAEAagAAZwAAZBIAZBMAZBQAZBUAZBYAZBcAZBgAZBkAZBoAZBsAZBwAZB0AZB4AZAsAZBwAZB8AZAMAZB0AZAgAZB4AZCAAZCEAZxYARF0VAH0AAHwAAGoEAGQiAIMBAF4CAHHGAIMBAEdIbgUAZCMAR0hkAABTKCQAAABOdAAAAAB0AQAAAF50AQAAADR0AQAAAEt0AQAAAGl0AQAAAC50AQAAAC90AQAAAE50AQAAAGp0AQAAAFB0AQAAAG90AQAAAD90AQAAAGx0AQAAADJ0AQAAAFRpAwAAAHMJAAAAWW91IHBhc3M6dAEAAABzdAEAAAB5dAEAAABudAEAAAB0dAEAAAA6dAEAAAB7dAEAAAB3dAEAAABxdAEAAABFdAEAAAA2dAEAAABmdAEAAABYdAEAAAB1dAEAAABhdAEAAAAxdAEAAAB9dAUAAABST1QxM3MFAAAATm8gOigoBQAAAHQEAAAAam9pbnQDAAAAY2hydAMAAABvcmR0CQAAAHJhd19pbnB1dHQGAAAAZGVjb2RlKAMAAAB0AQAAAGV0AwAAAHRtcHQGAAAAcGFzc3dkKAAAAAAoAAAAAHMHAAAAdGFzay5weVIcAAAAAgAAAHMKAAAAAAFfAQwBDAFvAQ=='.decode('base64')
code = marshal.loads(src)
exec code
```

We can take a look at the file and see that it uses the [Python][Python] [marshal] module to serialize some [Python] objects, which is originally [base64] encoded. If we wanted to, we could decode this and recreate the code as we needed to.

If you do this (perhaps within [IDLE]) and you get to create your `code` object, you can interact with it! It is a ton of [Python bytecode]. You can explore it completely with `dir(code)`, and from that, things like `code.co_consts` and `code.co_varnames` and more. 

If you check out the `code.co_varnames`, you should see the object has a variable named `passwd`.

We want to get to the value of that variable, right? 

Honestly I don't know a way to get it directly... but we can "disassemble" the [bytecode] and try and reverse engineer it. We can do this for [Python] code with the [`dis`][dis] module.

`dis.dis(code)` should give you an [Assembly]-like output. 


```
  3           0 LOAD_CONST               1 ('')
              3 LOAD_ATTR                0 (join)
              6 BUILD_LIST               0
              9 LOAD_CONST               2 ('^')
             12 LOAD_CONST               3 ('4')
             15 LOAD_CONST               4 ('K')
             18 LOAD_CONST               5 ('i')
             21 LOAD_CONST               6 ('.')
             24 LOAD_CONST               7 ('/')
             27 LOAD_CONST               8 ('N')
             30 LOAD_CONST               9 ('j')
             33 LOAD_CONST              10 ('P')
             36 LOAD_CONST              11 ('o')
             39 LOAD_CONST              12 ('?')
             42 LOAD_CONST              13 ('l')
             45 LOAD_CONST              14 ('2')
             48 LOAD_CONST              15 ('T')
             51 LOAD_CONST              12 ('?')
             54 BUILD_LIST              15
             57 GET_ITER            
        >>   58 FOR_ITER                28 (to 89)
             61 STORE_FAST               0 (e)
             64 LOAD_GLOBAL              1 (chr)
             67 LOAD_GLOBAL              2 (ord)
             70 LOAD_FAST                0 (e)
             73 CALL_FUNCTION            1
             76 LOAD_CONST              16 (3)
             79 BINARY_ADD          
             80 CALL_FUNCTION            1
             83 LIST_APPEND              2
             86 JUMP_ABSOLUTE           58
        >>   89 CALL_FUNCTION            1
             92 STORE_FAST               1 (tmp)

  4          95 LOAD_GLOBAL              3 (raw_input)
             98 LOAD_CONST              17 ('You pass:')
            101 CALL_FUNCTION            1
            104 STORE_FAST               2 (passwd)

  5         107 LOAD_FAST                2 (passwd)
            110 LOAD_FAST                1 (tmp)
            113 COMPARE_OP               2 (==)
            116 POP_JUMP_IF_FALSE      230

  6         119 LOAD_CONST               1 ('')
            122 LOAD_ATTR                0 (join)
            125 BUILD_LIST               0
            128 LOAD_CONST              18 ('s')
            131 LOAD_CONST              19 ('y')
            134 LOAD_CONST              20 ('n')
            137 LOAD_CONST              21 ('t')
            140 LOAD_CONST              22 (':')
            143 LOAD_CONST              23 ('{')
            146 LOAD_CONST              24 ('w')
            149 LOAD_CONST              25 ('q')
            152 LOAD_CONST              26 ('E')
            155 LOAD_CONST              27 ('6')
            158 LOAD_CONST              28 ('f')
            161 LOAD_CONST              29 ('X')
            164 LOAD_CONST              30 ('u')
            167 LOAD_CONST              11 ('o')
            170 LOAD_CONST              28 ('f')
            173 LOAD_CONST              31 ('a')
            176 LOAD_CONST               3 ('4')
            179 LOAD_CONST              29 ('X')
            182 LOAD_CONST               8 ('N')
            185 LOAD_CONST              30 ('u')
            188 LOAD_CONST              32 ('1')
            191 LOAD_CONST              33 ('}')
            194 BUILD_LIST              22
            197 GET_ITER            
        >>  198 FOR_ITER                21 (to 222)
            201 STORE_FAST               0 (e)
            204 LOAD_FAST                0 (e)
            207 LOAD_ATTR                4 (decode)
            210 LOAD_CONST              34 ('ROT13')
            213 CALL_FUNCTION            1
            216 LIST_APPEND              2
            219 JUMP_ABSOLUTE          198
        >>  222 CALL_FUNCTION            1
            225 PRINT_ITEM          
            226 PRINT_NEWLINE       
            227 JUMP_FORWARD             5 (to 235)

  7     >>  230 LOAD_CONST              35 ('No :(')
            233 PRINT_ITEM          
            234 PRINT_NEWLINE       
        >>  235 LOAD_CONST               0 (None)
            238 RETURN_VALUE        
```

Check it out, this should be easy enough to read; you can see that it joins a ton of characters, and then compares them with your input. That joined string must be the flag! 

And, we can see a 'ROT13' notion in the disassembly. Is that string [rot13]-ed?

Sure enough, if you compile and create the string `synt:{wqE6fXuofa4XNu1}` and then [rot13] it, you will get...

__`flag:{jdR6sKhbsn4KAh1}`__

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
[/etc/passwd]: https://en.wikipedia.org/wiki/Passwd#Password_file
[more]: https://en.wikipedia.org/wiki/More_(command)
[vi]: https://en.wikipedia.org/wiki/Vi
[vim]: http://www.vim.org/
[caesar cipher]: https://en.wikipedia.org/wiki/Caesar_cipher
[vignere cipher]: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
[substitution cipher]: https://en.wikipedia.org/wiki/Substitution_cipher
[DNA]: https://en.wikipedia.org/wiki/Nucleic_acid_sequence
[Python bytecode]: http://security.coverity.com/blog/2014/Nov/understanding-python-bytecode.html
[uncompyle]: https://github.com/gstarnberger/uncompyle
[Easy Python Decompiler]: https://github.com/aliansi/Easy-Python-Decompiler-v1.3.2
[marshal]: https://docs.python.org/2/library/marshal.html
[IDLE]: https://en.wikipedia.org/wiki/IDLE
[bytecode]: http://whatis.techtarget.com/definition/bytecode
[dis]: https://docs.python.org/2/library/dis.html
[rot13]: https://en.wikipedia.org/wiki/ROT13