__Repeated XOR__
===========

_John Hammond_ | _Thursday, December 22nd, 2016_ 

 
> There's a secret passcode hidden in the robot's "history of cryptography" module. But it's encrypted! Here it is, hex-encoded: [encrypted.txt](encrypted.txt). Can you find the hidden passcode? 

----------


So this challenge title, __Repeated XOR__, tells us that it is another [XOR] challenge; one of the simpler classic cryptography challenges. This time, though, different from the [__ZOR__](../zor) challenge that we saw before, it uses a _repeated_ key rather than just one single-byte key.

A lot of times in cyber you will see a recurring task and you just need to have a tool in your toolkit that you can use on it.

This is one of those tasks.

To solve repeated [XOR] challenges, you need to do a decent amount of [frequency analysis]. Honestly, I am not too good at this. But thankfully, Trey Maxam built a nice utility that attempt to break repeated [XOR] ciphers. He built this while going through the [Matasano Cryptopals] challenges.

His utilities isn't the most forgiving, and it requires that the ciphertext be [base64] encoded and in raw [hex] bytes. 

The ciphertext that they gives [`encrypted.txt`](encrypted.txt) is in "[hex]"... in that is just the characters that make up [hex]... but not the _raw_ [hex] bytes. And we still have to [base64] encode it. We can do this all easily in [Python].

``` python
>>> import base64
>>> c = base64.b64encode(open('encrypted.txt').read().decode('hex'))
>>> open('ciphertext.txt', 'w').write(c)
```

Now you should have a new file, [`ciphertext.txt`](ciphertext.txt), which has your [base64] encoded text.

```
uCONuh0HaxL74SWL8h1QYxeuoHnKqQ5XMBGt+HvM8F8DZkf9o3qZ/Q4DN0D68H7K/lkAMhH4y0a8vU8IaRS8tSSd6FgAdR/l4SSRu0kOdQq8rirYq08Ydwfzpj6ZuFUYK1PotiPYuFwTcxr5smyPp0gNY1PupCCB6EgRaB28oGyTrURBcxv9tWyMoFgYJwTztCCc6FgZZBv9ryud6F8EcwT5pCLYvFUEagD5rTqdux0DflPxpC2Wux0OYVP94T+dq0gTYl+8ozmM6FMOaV7/szWIvFIGdRLsqSWb5B0MYgf0rijW6HsOdVP5uS2VuFEEK1P94SqZq1hMcxyxpy2brR0MYhboqCKf6FITJxLy4SmAq1UAaRT57WyOoVxBZlPoszmLvFgFJxDztD6RrU9NJxDztCCc6F8EJwbvpCjW6GkJbgC8qimB5B0Wbxr/qWyap0kJJwP9sziRrU5BbBbstWyZqk4OawbopCCB6E4EZAH5tWDYq1IUaxe8tSSdph0DYlPpsimc6EkOJxbkoiSZploEJxbyoj6BuEkEY1PxpD+LqVoEdF28gGyWvVADYgG8rirYu1QGaRr6qC+ZpklBdwH9ojiRq1wNJxf1pyqRq0gNcxr5smyZulQSYlPrqDiQ6EkJbgC8oDyIulIAZBu8tSPYrFQScwH1ozmMoVMGJxj5uD/WwjcoaVOt+XvM5B0AJxHzrifYqkRB
. . . 
```


Next we will want to use Trey's tool. This is available in our [`tools`][tools] repository, and I have included it here in this folder. 

The tool is called [`breakRepeatedXOR.py`](breakRepeatedXOR.py). It takes _one_ argument, which is the [base64] encoded [hex] representation of the encrypted data... which in our case is our new [`ciphertext.txt`](ciphertext.txt)!

```
./breakRepeatedXOR.py ciphertext.txt
```

It will crank out a bunch of possible keylengths, with a given score. __The _lower_ the score, the most likely it is that it is the keylength.__ This is the [frequency analysis] in action, trying to determine what repeated lengths has the most likely occurence of the English language.

It will recommend a keylength (which is the minimum one), which you ought to use. Enter it in as your choice.

```
. . .
Keylength: 36       Score: 2.67841880342
Keylength: 37       Score: 4.14851485149
Keylength: 38       Score: 4.02175080559
Keylength: 39       Score: 3.9703525641
Keylength: 40       Score: 4.29032258065
Recomended: 27
Choose a key length: 27
```

So in our case, you should enter `27`.

It will then recommend specific keys, which it thinks are the possible keys used for the encryption and decryption. If you just hit the `Enter` key here, it will try all the keys (which is usually what you want to do).

Then, it will spit out all of the attempts to "decrypt" the cipher.

Here is what I received:

```
your flag is: 1dd2a52a367b19748bba4ab6a53b03f1226da5bd

During the early history of cryptography, two parties would rely upon a key that they would exchange between themselves by means of a secure, but non-cryptographic, method. For example, a face-to-face meeting or an exchange, via a trusted courier, could be used. This key, which both parties kept absolutely secret, could then be used to exchange encrypted messages. A number of significant practical difficulties arise with this approach to distributing keys.

In 1874, a book by William Stanley Jevons described the relationship of one-way functions to cryptography, and went on to discuss specifically the factorization problem used to create a trapdoor function. In July 1996, mathematician Solomon W. Golomb said: "Jevons anticipated a key feature of the RSA Algorithm for public key cryptography, although he certainly did not invent the concept of public key cryptography."

In 1970 James H. Ellis a British cryptographer at the Government Communications Headquarters (GCHQ) conceived of the possibility of "non-secret encryption", (now called public-key cryptography), but could see no way to implement it. In 1973 his colleague Clifford Cocks invented what has become known as the RSA encryption algorithm, giving a practical method of implementation, and in 1974 another GCHQ mathematician and cryptographer, Malcolm J. Williamson developed what is now known as Diffie-Hellman key exchange. None of these appear to have been put to practical use, and their early invention did not become public knowledge until the research was declassified by the British government in 1997.

In 1976 an asymmetric-key cryptosystem was published by Whitfield Diffie and Martin Hellman who, influenced by Ralph Merkle's work on public-key distribution, disclosed a method of public-key agreement. This method of key exchange, which uses exponentiation in a finite field, came to be known as Diffie-Hellman key exchange. This was the first published practical method for establishing a shared secret-key over an authenticated (but not private) communications channel without using a prior shared secret. Merkle's "public-key-agreement technique" became known as Merkle's Puzzles, and was invented in 1974 and published in 1978.

In 1977 a generalization of Cocks's scheme was independently invented by Ron Rivest, Adi Shamir and Leonard Adleman, all then at MIT. The latter authors published their work in 1978, and the algorithm came to be known as RSA, from their initials. RSA uses exponentiation modulo a product of two very large primes, to encrypt and decrypt, performing both public key encryption and public key digital signature. Its security is connected to the extreme difficulty of factoring large integers, a problem for which there is no known efficient general technique. In 1979, Michael O. Rabin published a related cryptosystem that is probably secure as long as the factorization of the public key remains difficult - it remains an assumption that RSA also enjoys this security.

Since the 1970s, a large number and variety of encryption, digital signature, key agreement, and other techniques have been developed in the field of public-key cryptography. The ElGamal cryptosystem, invented by Taher ElGamal relies on the similar and related high level of difficulty of the discrete logarithm problem, as does the closely related DSA, which was developed at the US National Security Agency (NSA) and published by NIST as a proposed standard.

The introduction of elliptic curve cryptography by Neal Koblitz and Victor Miller, independently and simultaneously in the mid-1980s, has yielded new public-key algorithms based on the discrete logarithm problem. Although mathematically more complex, elliptic curves provide smaller key sizes and faster operations for approximately equivalent estimated security.
```


That looks like English!

And at the very top, we can see our flag. Thanks for the win, Trey!

__You should add this tool to your arsenal. Know that it will usually do an excellent job of solving repeated [XOR] challenges.__

__Submit: `1dd2a52a367b19748bba4ab6a53b03f1226da5bd`__

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
[hexadecimal]: https://en.wikipedia.org/wiki/Hexadecimal
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
[Cryptography]: https://en.wikipedia.org/wiki/Cryptography
[bitwise]: https://en.wikipedia.org/wiki/Bitwise_operation
[bitwise operation]: https://en.wikipedia.org/wiki/Bitwise_operation
[bitwise operations]: https://en.wikipedia.org/wiki/Bitwise_operation
[pwntools]: https://github.com/Gallopsled/pwntools
[pwnlib]: https://github.com/Gallopsled/pwntools
[pwn]: https://github.com/Gallopsled/pwntools
[frequency analysis]: https://en.wikipedia.org/wiki/Frequency_analysis
[Matasano]: https://cryptopals.com/
[Matasano Cryptopals]: https://cryptopals.com/
[Cryptopals]: https://cryptopals.com/
[tools]: https://github.com/uscga/tools