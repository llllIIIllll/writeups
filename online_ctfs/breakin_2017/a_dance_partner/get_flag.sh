#!/bin/bash

./process_image.py 2>/dev/null > the_text.txt
md5sum the_text.txt | cut -d " " -f1

