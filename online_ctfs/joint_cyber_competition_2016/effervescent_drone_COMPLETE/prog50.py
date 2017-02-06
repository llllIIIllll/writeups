#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-14 09:25:31
# @Last Modified by:   john
# @Last Modified time: 2016-05-14 09:26:37



def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

print ",".join(fizzbuzz(n) for n in xrange(1, 1001))