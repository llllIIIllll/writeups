#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-05-01 11:44:49
# @Last Modified by:   john
# @Last Modified time: 2016-05-01 11:48:49

import subprocess as shell
import os
import re

repo_url = 'https://github.com/l33tdev42/testApp'
repo_dir = repo_url.split('/')[-1]

os.chdir(repo_dir)
content = shell.check_output('git show'.split())

matched = re.search('CTF{.*}', content, re.IGNORECASE)
if matched:
	print matched.group()