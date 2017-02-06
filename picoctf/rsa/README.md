__RSA__
===========

_John Hammond_ | _Saturday, December 2nd, 2016_ 

 
> A Daedalus Corp spy sent an RSA-encrypted message. We got their key data, but we're not very good at math. Can you decrypt it? Here's the data. Note that the flag is not a number but a number decoded as ASCII text. 


----------

So I am nowhere near as brilliant with [RSA] and [cryptography] as Trey is, so I had avoided this challenge for a long long while. After Trey has done a few presentations and has walked me through the process a few times (thank you), I felt a lot more comfortable with [RSA] and thought I would at least look at this challenge.

When I extracted the archive I did not realize it would be so easy. They gave us literally everything we needed to solve the problem, we just had to run one exponent, the formula to decrypt. We didn't even have to factor `N` to try and fine `p` or `q` or try and get `phi`. They gave us `d`, which in our eyes, is essentially the [private key].


You can download the data they give you as [`handout.tgz`](handout.tgz).

You can extract everything like so:

```
gunzip handout.tgz
tar xfv handout.tar
```

You should now have files, [`ciphertext.txt`](ciphertext.txt) and [`key_data.txt`](key_data.txt). Look at these to grab your ingredients for the [RSA] recipe.

``` python
N = 0xb197d3afe713816582ee988b276f635800f728f118f5125de1c7c1e57f2738351de8ac643c118a5480f867b6d8756021911818e470952bd0a5262ed86b4fc4c2b7962cd197a8bd8d8ae3f821ad712a42285db67c85983581c4c39f80dbb21bf700dbd2ae9709f7e307769b5c0e624b661441c1ddb62ef1fe7684bbe61d8a19e7
e = 65537
p = 0xc315d99cf91a018dafba850237935b2d981e82b02d994f94db0a1ae40d1fc7ab9799286ac68d620f1102ef515b348807060e6caec5320e3dceb25a0b98356399
q = 0xe90bbb3d4f51311f0b7669abd04e4cc48687ad0e168e7183a9de3ff9fd2d2a3a50303a5109457bd45f0abe1c5750edfaff1ad87c13eed45e1b4bd2366b49d97f
d = 0x496747c7dceae300e22d5c3fa7fd1242bda36af8bc280f7f5e630271a92cbcbeb7ae04132a00d5fc379274cbce8c353faa891b40d087d7a4559e829e513c97467345adca3aa66550a68889cf930ecdfde706445b3f110c0cb4a81ca66f8630ed003feea59a51dc1d18a7f6301f2817cb53b1fb58b2a5ad163e9f1f9fe463b901

c = 0x58ae101736022f486216e290d39e839e7d02a124f725865ed1b5eea7144a4c40828bd4d14dcea967561477a516ce338f293ca86efc72a272c332c5468ef43ed5d8062152aae9484a50051d71943cf4c3249d8c4b2f6c39680cc75e58125359edd2544e89f54d2e5cbed06bb3ed61e5ca7643ebb7fa04638aa0a0f23955e5b5d9
```

Now you have all the ingredients! And look, they seriously just _give_ you `d`, what we consider the [private key]. All we need to do is run our decryption formula and we get the flag.


If you need a more indepth explanation of some of [RSA], here is some insanely documented [Python] code that tries to walk you through the whole process:

``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-25 14:33:10
# @Last Modified by:   john
# @Last Modified time: 2016-12-03 11:16:39

from Crypto.Util.number import getPrime
import binascii
import primefac

'''
This Python code tries to illustrate how RSA is done at a basic level.
'''


# At RSA's core, there are two PRIME factors, p and q.
# With this code, I just generate two large random prime numbers.
# p and q are typically NOT given to you in an RSA challenge.
bits_size = 256
p = getPrime( bits_size )
q = getPrime( bits_size )


# These two prime factors multiply to create n, which is "the modulus".
# n is typically GIVEN to you in an RSA challenge.
n = p * q


# The plaintext is typically referred to as m. Since we are working 
# with numbers and math, we treat the string information as hex.
# Obviously this is NEVER given to you in an RSA challenge.
m = "This is the clear text message."
m = binascii.hexlify(m)
m = int(m, 16)


# Another value, called e, is "the exponent".
# Both e and n make up "the public key", which is meant to be common
# knowledge. This is why typically n and e are BOTH GIVEN in an RSA challenge.
# Typcially, e is 65537, which is 0x10001 in hex
e = 0x10001


# The ciphertext, c, is created by this ENCRYPTION formula here.
#    c = ( m ^ e ) % n
# See how e is the exponent and n is the modulus?
# That is how the ENCRYPTION takes place.
# Typically you are given the c in an RSA challenge and it is your task
# to DECRYPT it to the m value, the plaintext.
c = pow( m, e, n )


# Now how do we decrypt? We need "the private key"....
# We call this d in RSA. Thanks to some handy mathematical functions,
# you can find "Euler's Totient", or "the Phi function" of a number.
# This is 'the number of numbers that are less than a certain number and share
# a common denominator with that certain number'.
# I know that is hard to wrap your mind around here, but thankfully it is MUCH
# easier for a prime number. For a prime number, it is simply that number minus 1!

# So, if you are given n, what you need to do is find the factors of n. 
# Like we've seen, this is typically p and q. So, can we find the phi function
# of n? Well, n is prime, and so are its factors, p and q, so phi should just be: 
phi = ( q - 1 ) * ( p - 1 )


# Now, we can kind of unravel that modular arithmetic that was done during the
# ENCRYPTION formula. We can find the private key, d, with the MODULAR INVERSE,
# of e and phi.  
# I use a module to do this that is reworked to use Trey's function
#     https://github.com/JohnHammond/primefac_fork
d = primefac.modinv( e, phi )

# Now, we can do a similar thing like before, but this time for DECRYPTION.
#        m = ( c ^ d ) % n
# This time we raise to our private key as an exponent, but still take the modulus.
# And we have successfully decrypted RSA!
m = pow( c, d, n )
print repr(binascii.unhexlify(hex(m)[2:-1]))
```

Now, we can do that with the numbers that we have, for this challenge specifically, not just for the general case. The code to do that is in the [`get_flag.py`](get_flag.py) script, and shown here:

``` python
#!/usr/bin/env python

import primefac
import binascii

N = 0xb197d3afe713816582ee988b276f635800f728f118f5125de1c7c1e57f2738351de8ac643c118a5480f867b6d8756021911818e470952bd0a5262ed86b4fc4c2b7962cd197a8bd8d8ae3f821ad712a42285db67c85983581c4c39f80dbb21bf700dbd2ae9709f7e307769b5c0e624b661441c1ddb62ef1fe7684bbe61d8a19e7
e = 65537
p = 0xc315d99cf91a018dafba850237935b2d981e82b02d994f94db0a1ae40d1fc7ab9799286ac68d620f1102ef515b348807060e6caec5320e3dceb25a0b98356399
q = 0xe90bbb3d4f51311f0b7669abd04e4cc48687ad0e168e7183a9de3ff9fd2d2a3a50303a5109457bd45f0abe1c5750edfaff1ad87c13eed45e1b4bd2366b49d97f
d = 0x496747c7dceae300e22d5c3fa7fd1242bda36af8bc280f7f5e630271a92cbcbeb7ae04132a00d5fc379274cbce8c353faa891b40d087d7a4559e829e513c97467345adca3aa66550a68889cf930ecdfde706445b3f110c0cb4a81ca66f8630ed003feea59a51dc1d18a7f6301f2817cb53b1fb58b2a5ad163e9f1f9fe463b901

c = 0x58ae101736022f486216e290d39e839e7d02a124f725865ed1b5eea7144a4c40828bd4d14dcea967561477a516ce338f293ca86efc72a272c332c5468ef43ed5d8062152aae9484a50051d71943cf4c3249d8c4b2f6c39680cc75e58125359edd2544e89f54d2e5cbed06bb3ed61e5ca7643ebb7fa04638aa0a0f23955e5b5d9

m = pow( c, d, N )
print repr(binascii.unhexlify(hex(m)[2:-1]))
```

We can run this code and get...

```
'Congratulations on decrypting an RSA message! Your flag is modular_arithmetics_not_so_bad_after_all'
```




__Submit: `modular_arithmetics_not_so_bad_after_all!`__

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