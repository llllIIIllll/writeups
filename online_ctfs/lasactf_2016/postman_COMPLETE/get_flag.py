#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-03-19 19:45:03
# @Last Modified by:   john
# @Last Modified time: 2016-03-19 19:46:53

import urllib2

address = 'http://web.lasactf.com:45025/'

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Google Ultron'),
                     ('SpecialAuth', 'Kyle'),
                     ('Referer', 'kyleisacoolguy.org')]
response = opener.open(address)

print response.read().split(':')[-1].replace('</h1>','')
