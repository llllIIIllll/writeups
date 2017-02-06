#!/bin/bash

strings recovered.img|grep "flag"|head -n 1| sed 's/flag{//' | sed 's/}//g'
