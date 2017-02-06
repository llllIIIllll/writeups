#!/bin/bash

nslookup -type=txt search.icec.tf|grep -o "IceCTF{.*}"
