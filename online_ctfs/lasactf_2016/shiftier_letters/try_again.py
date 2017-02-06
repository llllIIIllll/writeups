#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 21:19:26
# @Last Modified by:   john
# @Last Modified time: 2016-03-21 13:33:06

from pwn import *
from colorama import *
from collections import deque
from threading import Thread
import time
import random
import enchant
from enchant.checker import SpellChecker
import string

init(autoreset=True)
d = enchant.Dict('en_US')
host = 'web.lasactf.com'
port = 4056
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

spellcheck = SpellChecker('en_US')


def attempt(challenge, max_incorrect=1):
    # max_incorrect = 1
    minimum = [100, 0]
    challenge = challenge
    for i in range(26):
        found = False
        incorrect_words = []
        shifted = rotate(challenge, i)
        spellcheck.set_text(shifted)
        for error in spellcheck:
            # print "ERROR WITH WORD", error.word
            incorrect_words.append(error.word)

        num_words = len(shifted.split())
        num_wrong = len(incorrect_words)
        # print num_wrong, minimum
        if (num_wrong < minimum[0] and num_wrong <= num_words - max_incorrect):
            # print "num_words", num_words, "num_wrong", num_wrong
            minimum = num_wrong, i,
            found = True
            print Fore.MAGENTA + "max_incorrect", max_incorrect, "minimum", minimum
        if found:
            use = rotate(challenge, minimum[1])
            if minimum == (0, 0):
                print "THIS IS WHEN IT BREAKS"
                attempt(challenge, max_incorrect + 1)
            else:
                return use
                break
    print Fore.CYAN + "could not get solution with pyenchant, trying dictionary"

    for i in range(26):
        shifted = rotate(challenge, i)
        shifted_words = shifted.split()
        incorrect_words.append(error.word)
        for word in shifted_words:
            if word not in words:
                incorrect_words.append(word)

        num_words = len(shifted.split())
        num_wrong = len(incorrect_words)
        # print num_wrong, minimum
        if (num_wrong < minimum[0] and num_wrong <= num_words - max_incorrect):
            # print "num_words", num_words, "num_wrong", num_wrong
            minimum = num_wrong, i,
            found = True
            print Fore.MAGENTA + "max_incorrect", max_incorrect, "minimum", minimum
        if found:
            use = rotate(challenge, minimum[1])
            return use
            break
    return Fore.RED + "could not get solution with dictionary"


# while (True):
    # try:
s = tubes.remote.remote(host, port)
for i in range(100):
    print Fore.BLUE + str(i),
    received = s.recv().strip()
    print Fore.YELLOW + "received " + str(received.split()[:3]),
    sending = attempt(received)
    print Fore.YELLOW + "sending " + str(sending.split()[:3])
    s.sendline(sending)
s.close()
    # except:
    #     print Style.BRIGHT + Fore.RED + "ONE LOSS"
    #     continue
