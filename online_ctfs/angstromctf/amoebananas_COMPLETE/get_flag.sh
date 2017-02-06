#!/bin/bash

curl "http://web.angstromctf.com:1337/" 2>/dev/null|grep "flag"|rev|cut -d " " -f2|rev
