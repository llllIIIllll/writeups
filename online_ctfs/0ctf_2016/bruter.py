#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-13 18:15:18
# @Last Modified by:   john
# @Last Modified time: 2016-03-13 21:14:43

import hashlib
import string
from colorama import *
import sys

starts = sys.argv[1]
init(autoreset=True)

your_list = string.printable
complete_list = []
for current in xrange(7):
    a = [i for i in your_list]
    for y in xrange(current):
        a = [x+i for i in your_list for x in a]
    for each in a:
        m = hashlib.md5()
        m.update(each)
        hashed = m.hexdigest()
        # print each, Fore.YELLOW + hashed
        if hashed.startswith(starts):
            print each, Fore.GREEN + hashed
            raw_input()
