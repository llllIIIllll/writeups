#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-20 08:15:25
# @Last Modified by:   john
# @Last Modified time: 2016-02-20 08:25:21

import pwnlib
import sympy
from colorama import *
from time import sleep

host = '188.166.133.53'
port = 11027

connection = pwnlib.tubes.remote.remote( host, port )

print connection.recv()
sleep(.1)
equation = connection.recv()
sleep(.1)
print equation

equation = equation.split(':')[-1].strip()
x = sympy.symbols('x')
left_hand_side, right_hand_side = equation.split('=')

#print left_hand_side, right_hand_side
left_hand_side = sympy.sympify(left_hand_side)
right_hand_side = sympy.sympify(right_hand_side)


print sympy.solve(sympy.Eq(left_hand_side, right_hand_side))[0]

connection.close()