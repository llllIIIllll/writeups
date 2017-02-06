#!/usr/bin/env python

import binascii

first = '3337cec1efcefdd0d8ccfbdba089d5c2bae6f185badaf589edc1fbddbddabaddf2ccbac3f5cbb4'

second = '34318fb3a3b9abbdaeb9f7fc84a8eaafedbba2b2a3bdedbea8fcacfcafb5aafcafbda3b7edb6a2bee3fced'

third = '35346bfd47f74ff34af713b26af345fe09a71ca704a018ab1cbc09b27dfa4cfc09e64cfe45b25dfa4cff09e641f709e248e15ae546e04dbc'

fourth = '3539cae7e6edeee9ebedb2a8c1fcaffba8aac5e7fae1e9fafcf1aaa6a8a8dce0edf1afe4e4a8fcede4e4a8f1e7fda8ffe0edfaeda8fce7a8e5ededfca6'

ciphers = [ first, second, third, fourth ]

for cipher in ciphers:
	b = binascii.unhexlify(cipher)
	print b



from collections import Counter
import operator
import enchant

import os


english_letter_frequencies = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

def get_frequency_list_from_raw_bytes(raw_bytes):
	# This will return a list of all the characters sorted in descending
	# order of frequency
	frequencies = Counter(raw_bytes)
	# print frequencies
	sorted_x = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)
	cipher_frequency_list = [ byte[0] for byte in sorted_x ]
	return cipher_frequency_list

def xor_string_with_a_single_byte(string, byte):

	return ''.join([ chr( ord(c) ^ byte ) for c in string ])

def english_score_a_string(string):
	# The LOWER (the MORE NEGATIVE) a score is, the better it is!!!

	d = enchant.Dict()

	weight = 20

	score = 0
	string = string.upper()
	for character in string:
		character_count = string.count(character)
		
		if ord(character) <= 33 or ord(character) >= 126:
			# NOT A PRINTABLE CHARACTER?!!?
			score += weight
		if character in english_letter_frequencies:
			score -= english_letter_frequencies[character]

	if ( score > 0 ):
		# There is no where near enough English characters in this...
		return score 

	words = string.split()
	number_of_words = len(words)

	for word in words:
		try:
			if d.check(word):
				score -= weight*2
			else:
				# Not a real word!!
				score += weight
		except:
			# Woah, something is SUPER wrong.
			break

	del d
	return score

def break_single_byte_xor_of_hex_string(hex_input):

	raw_bytes = binascii.unhexlify(hex_input)

	scores = []
	print "Brute-forcing with all 255 ASCII characters... (may be a while)"
	for single_byte in range(255):
		new_string = xor_string_with_a_single_byte(raw_bytes, single_byte)
		# print new_string
		score =  english_score_a_string(new_string)
		scores.append( ( score, new_string ) )
		# print min(scores)[0], len(raw_bytes), min(scores)[-1]
		if ( score < len(raw_bytes)*-6 ):
			return min(scores)[-1]
	return min(scores)


# print break_single_byte_xor_of_hex_string(first)

for cipher in ciphers:
	print break_single_byte_xor_of_hex_string(cipher)