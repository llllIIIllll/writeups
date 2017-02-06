#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-02-21 21:56:42
# @Last Modified by:   john
# @Last Modified time: 2016-02-21 22:01:37

from colorama import *

string = '''
. . . . . . . . . . . . . . .
. . . . . ! ? ! ! . ? . . . .
. . . . . . . . . . . . . . .
. ? . ? ! . ? . . . . . . . .
! . ? . . . . . . . ! ? ! ! .
? . . . . . . ? . ? ! . ? . .
. . . . . . . . ! . ! ! ! ! !
! ! . . . ! . . . . . . . . .
. . . . ! . ? . . . . . . . !
? ! ! . ? ! ! ! ! ! ! ? . ? !
. ? ! ! ! ! ! . . . . . . . .
. . . . . ! . . . . . ! . ? .
. . . . . . . . ! ? ! ! . ? !
! ! ! ! ! ! ! ? . ? ! . ? ! .
! ! ! ! ! ! ! ! ! . ! . ? . .
. . . . . . . ! ? ! ! . ? . .
. . . . . . ? . ? ! . ? . . .
. . . . . . . . . ! . ! ! ! !
! . ? . . . . . . . . . ! ? !
! . ? ! ! ! ! ! ! ! ! ? . ? !
. ? ! . ! ! ! ! ! ! ! ! ! ! !
. . . ! . . . . . . . . . . .
! . ! ! ! . ! ! ! ! ! ! ! ! !
. ? . . . . . . . . . ! ? ! !
. ? . . . . . . . . ? . ? ! .
? ! . ! ! ! ! ! ! ! ! ! . ! !
! ! ! ! ! ! ! ! ! ! ! ! ! ! !
. . . . . . . . . . . . . ! .
'''

print Style.BRIGHT
for character in string:
	if character == ' ': continue
	if character == '\n': print ''
	if character == '.': print Back.RED + character,
	if character == '!': print Back.BLUE + character,
	if character == '?': print Back.GREEN + character,
