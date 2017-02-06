#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2017-01-21 18:09:14
# @Last Modified by:   john
# @Last Modified time: 2017-01-22 15:38:28


from pwn import *
import re
context.log_level = 'critical'

host = 'quizz.teaser.insomnihack.ch'
port = 1031

s = tubes.remote.remote( host, port )


'''
FLAG FOUND TO BE:
INS{GENUINE_CRYPTOGRAPHER_BUT_NOT_YET_A_PROVEN_SKILLED_ONE}
'''


birth_years = {
	"Ron Rivest"			:	 	"1947",
	"Daniel J. Bernstein"	: 		"1971",
	"Horst Fiestel"			:		"1915",
	"Antoine Joux"			:		"1967",
	"Jacques Stern"			:		"1949",
	"Arjen K. Lenstra"		:		"1956",
	"Nigel P. Smart"		:		"1967",
	"Yehuda Lindell"		:		"1971",
	"Markus Jakobsson"		:		"1968",
	"Ross Anderson"			:		"1956",
	"Kaisa Nyberg"			:		"1948",
	"Martin Hellman"		:		"1945",
	"Michael O. Rabin"		:		"1931",
	"David Naccache"		:		"1967",
	"Eli Biham"				:		"1960",
	"Paul Kocher"			:		"1973",
	"Joan Daemen"			:		"1965",
	"Ralph Merkle"			:		"1952",
	"Victor S. Miller"		:		"1947",
	"Douglas Stinson"		:		"1956",
	"Dan Boneh"				:		"1969",
	"Tatsuaki Okamoto"		:		"1952",
	"Yvo Desmedt"			:		"1956",
	"Jim Massey"			:		"1934",
	"Mitsuru Matsui"		:		"1961",
	"Donald Davies"			:		"1924",
	"Xuejia Lai"			:		"1954",
	"Amos Fiat"				:		"1956",
	"Adi Shamir"			:		"1952",
	"Shai Halevi"			:		"1966",
	"Alex Biryukov"			:		"1969",
	"Daniel Bleichenbacher"	:		"1964",
	"Lars Knudsen"			:		"1962",
	"Serge Vaudenay"		:		"1968",
	"Ronald Cramer"			:		"1968",
	"Whitfield Diffie"		:		"1944",
	"Rafail Ostrovsky"		:		"1963",
	"Claus-Peter Schnorr"	:		"1943",
	"Moni Naor"				:		"1961",
	"Phil Rogaway"			:		"1962",
	"Niels Ferguson"		:		"1965",
	"Paul van Oorschot"		:		"1962",
	"Jacques Patarin"		:		"1965",
	"Horst Feistel"			:		"1915",


	}
s.recv()
while (True):
	name = s.recv()
	print name
	
	found = re.findall('What is the birth year of (.*?) \?', name )
	if len(found) == 1:
		name = found[0]
		
		print name
		if ( name in birth_years.keys() ):

			# print "have name"
			s.sendline(birth_years[name])
			# print s.recvall()
			# print s.recv

		else:
			print "NO NAME", name
			break
	else:
		continue

s.close()