#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 21:58:42
# @Last Modified by:   john
# @Last Modified time: 2016-03-19 22:20:34

# from googlesearch import GoogleSearch

# results = GoogleSearch('irc zartik help')

# print results.top_results()[-1]

import pygoogle
g = pygoogle.pygoogle('zartik', 20)
print '*Found %s results*'%(g.get_result_count())

print g.display_results()