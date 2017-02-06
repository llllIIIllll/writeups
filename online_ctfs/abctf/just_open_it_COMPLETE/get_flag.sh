#!/bin/bash
# @Author: john
# @Date:   2016-07-17 08:47:06
# @Last Modified by:   john
# @Last Modified time: 2016-07-17 08:47:42

strings 676F6F645F6A6F625F6275745F746869735F69736E745F7468655F666C6167.jpg| grep -Eo "ABCTF{.*}"