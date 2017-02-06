#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ebuckley
# @Last Modified by:   john
# found online at https://gist.github.com/ebuckley/1842461

morseAlphabet = {'A': '.-',              'a': '.-',
                 'B': '-...',            'b': '-...',
                 'C': '-.-.',            'c': '-.-.',
                 'D': '-..',             'd': '-..',
                 'E': '.',               'e': '.',
                 'F': '..-.',            'f': '..-.',
                 'G': '--.',             'g': '--.',
                 'H': '....',            'h': '....',
                 'I': '..',              'i': '..',
                 'J': '.---',            'j': '.---',
                 'K': '-.-',             'k': '-.-',
                 'L': '.-..',            'l': '.-..',
                 'M': '--',              'm': '--',
                 'N': '-.',              'n': '-.',
                 'O': '---',             'o': '---',
                 'P': '.--.',            'p': '.--.',
                 'Q': '--.-',            'q': '--.-',
                 'R': '.-.',             'r': '.-.',
                 'S': '...',             's': '...',
                 'T': '-',               't': '-',
                 'U': '..-',             'u': '..-',
                 'V': '...-',            'v': '...-',
                 'W': '.--',             'w': '.--',
                 'X': '-..-',            'x': '-..-',
                 'Y': '-.--',            'y': '-.--',
                 'Z': '--..',            'z': '--..',
                 '0': '-----',           ',': '--..--',
                 '1': '.----',           '.': '.-.-.-',
                 '2': '..---',           '?': '..--..',
                 '3': '...--',           ';': '-.-.-.',
                 '4': '....-',           ':': '---...',
                 '5': '.....',           "'": '.----.',
                 '6': '-....',           '-': '-....-',
                 '7': '--...',           '/': '-..-.',
                 '8': '---..',           '(': '-.--.-',
                 '9': '----.',           ')': '-.--.-',
                 ' ': '/',               '_': '..--.-',
                 '/': " ",               ' ': ''
                 }

inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())

testCode = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.-- "


# parse a morse code string positionInString is the starting point for decoding
def decodeMorse(code, positionInString=0):


    return ''.join([ inverseMorseAlphabet[morseLetter] for morseLetter in code.split() ])


#encode a message in morse code, spaces between words are represented by '/'
def encodeToMorse(message):
    encodedMessage = ""
    for char in message[:]:
        encodedMessage += morseAlphabet[char.upper()] + " "

    return encodedMessage
