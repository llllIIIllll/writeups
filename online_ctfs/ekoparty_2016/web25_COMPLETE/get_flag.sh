#!/bin/bash

# the flag is referred to in the robots.txt file of the website

# https://ctf.ekoparty.org/robots.txt
# reads...
#
# User-agent: *
# Disallow: /static/wIMti7Z27b.txt
#

curl "https://ctf.ekoparty.org/static/wIMti7Z27b.txt"
