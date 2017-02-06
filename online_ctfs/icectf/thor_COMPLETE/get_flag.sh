#!/bin/bash

xxd -r thor_7101f3b9690d5dc6c3afefa49d82e0526b278ec1c564139369ad22c28721d4cf.txt > recovered
lzip -d recovered
eog recovered.out
