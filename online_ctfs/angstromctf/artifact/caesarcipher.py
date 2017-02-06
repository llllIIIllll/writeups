#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-10 19:57:46
# @Last Modified by:   john
# @Last Modified time: 2016-04-16 08:30:22

import string
import collections


process = '''
"gxipzhx qs kpz ravv mbgp gxs jmgk pe lps:
gxipzhx qs kpz ravv mbgp sgsibac ramb:
gxipzhx qs aqpbh gxs rsprcs cpvg epi aks.
fzvgmjs gxs epzbnsi pe qk eauimj qposn:
gp isai qs lav gxs gavt pe rplsi nmombs,
vzrisqsvg lmvnpq, abn rimqsoac cpos.
usepis qs gxmbhv jisags lsis bpbs, vaos gxmbhv
sgsibac, abn sgsibac m vxacc sbnzis.
acc xprs auabnpb, ks lxp sbgsi xsis."

gxs ecah mv jcavvmjv_ais_aclakv_mb_vgkcs
'''

def rotate(rotate_string, number_to_rotate_by):

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))


for i in range(26):
    print i, rotate(process, i)
