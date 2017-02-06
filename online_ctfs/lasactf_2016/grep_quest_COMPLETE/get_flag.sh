#!/bin/bash

SCRIPT='
# your commands
cd /problems/grep-quest_0/grepy-words/
grep -R "lasa"|cut -d ":" -f2
'


sshpass -p 'uscgabears' ssh -q objEEdump@shell.lasactf.com "$SCRIPT"
