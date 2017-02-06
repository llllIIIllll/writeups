#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2016-11-17 13:41:44
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-11-17 13:48:55


'''
The solution here is to 

1. Use easy_python_decompiler to get the original .py source code.

2. It uses a 'marshal' serialized object that is originally base64 encoded

3. Run the code enough to the point where you have the `code` object.

4. This is a ton of Python bytecode. You can explore it completely with
   dir(code), and from that, things like `code.co_consts` and `code.co_varnames`
   and more. 

5. You will notice that the object has a variable name called "passwd". 

6. We want to get the value of that variable, right?

7. I don't know of a way to get it directly, yet, because we "disassemble" the
   bytecode and try and reverse engineer it. We can do this with the `dis` module

8. `dis.dis(code)` should give you an Assembly like output. 
    You can see it joins a ton of characters and compares them. That joined string
    must be the flag... with a ROT13 on it! (You can find that as well.)

9. After ROT13-ing that string, you should get:

		synt:{wqE6fXuofa4XNu1} 

		 becomes...

		flag:{jdR6sKhbsn4KAh1}
'''


