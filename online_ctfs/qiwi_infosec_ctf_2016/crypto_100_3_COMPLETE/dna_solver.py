#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2016-11-18 12:51:23
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-11-18 13:12:51

mapping = {
		
		'CGA': 'A',
		'CCA': 'B',
		'GTT': 'C',
		'TTG': 'D',
		'GGC': 'E',
		'GGT': 'F',
		'TTT': 'G',
		'CGC': 'H',
		'ATG': 'I',
		'AGT': 'J',
		'AAG': 'K',
		'TGC': 'L',
		'TCC': 'M',
		'TCT': 'N',
		'GGA': 'O',
		'GTG': 'P',
		'AAC': 'Q',
		'TCA': 'R',
		'ACG': 'S',
		'TTC': 'T',
		'CTG': 'U',
		'CCT': 'V',
		'CCG': 'W',
		'CTA': 'X',
		'AAA': 'Y',
		'CTT': 'Z',
		'ATA': ' ',
		'TCG': ',',
		'GAT': '.',
		'GCT': ':',
		'ACT': '0',
		'ACC': '1',
		'TAG': '2',
		'GCA': '3',
		'GAG': '4',
		'AGA': '5',
		'TTA': '6',
		'ACA': '7',
		'AGG': '8',
		'GCG': '9'
}


def decode_dna( string ):

	pieces = []
	for i in range( 0, len(string), 3 ):
		piece =  string[i:i+3]
		# pieces.append()
		pieces.append( mapping[piece] )

	return "".join(pieces)


string = 'GGTTCAATGGGCTTGTCAATGGTTCGCATATCCATGGGCACGGTTCGCGGCTCA'	
print decode_dna(string)

