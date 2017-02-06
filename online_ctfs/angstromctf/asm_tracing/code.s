# This ASM is AT&T syntax: http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
# All the GNU tools (as, gdb, and objdump) use AT&T syntax by default
start:
	mov $1337, %eax
	mov $6098, %ebx
	mov $4352, %ecx
	xor %edx, %edx
	
	sub %ecx, %ebx
	cmp %ebx, %eax
	jge next1
	jmp next2
next1:
	cmp $4, %edx
	jg end
	inc %edx
next2:
	xchg %eax, %ebx
	idiv %ebx
	add %edx, %eax
	imul %ecx
	jmp next1
end:



# =======================================================

eax = 1337
ebx = 6098
ecx = 4352
edx = 0

ebx = ebx - ecx = 6098 - 4352 = 1746
if ( eax >= ebx )
if ( 1337 >= 1746 ){


}
else{
	eax = 1746
	ebx = 1337
	eax / ebx = 
		eax = 1
		edx = 409
	


}