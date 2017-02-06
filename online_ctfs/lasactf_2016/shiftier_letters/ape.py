#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 21:19:26
# @Last Modified by:   john
# @Last Modified time: 2016-03-20 00:34:30

from pwn import *
import time
import random
from threading import Thread
import enchant

d = enchant.Dict('en_US')

from colorama import *
init(autoreset=True)

host = 'web.lasactf.com'
port = 4056

from collections import deque
import string

dictionary = open('/usr/share/dict/words')
words = dictionary.read().split('\n')
dictionary.close()


def rotate(rotate_string, number_to_rotate_by):

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))


def brute_force_cipher(challenge_string):
    for i in range(len(string.ascii_uppercase)):
        print i, rotate(challenge_string, i)


all_found = []
s = tubes.remote.remote(host, port)
complete = False
while (True):

    complete = False
    received = s.recv()
    print Fore.YELLOW + "received", received

    counts = []
    for offset in range(len(string.ascii_uppercase)+1):
        count = 0
        # print i, rotate(challenge_string, i)
        rotated_string = rotate(received, offset)
        # counts.append([count, offset, rotated_string])
        if complete:  break
        for i in range(3):
            words = rotated_string.split()
            random.shuffle(words)
            if complete:  break
            for word in words:
                # print "looking at word", word
                # print word
                if complete:  break
                if d.check(word):
                    # counts[-1][0] += 1
                    count += 1
                    if complete:  break
                    if count >= 6:
                        # print "WORD", rotated_string
                        final = rotated_string
                        count = 0
                        print Fore.BLUE + "sending", final
                        s.send(final)
                        complete = True
                        break
    # try:
    #     print Fore.BLUE + "sending", final
    #     s.send(final)
    #     del final
    # except:
    #     continue

s.close()
