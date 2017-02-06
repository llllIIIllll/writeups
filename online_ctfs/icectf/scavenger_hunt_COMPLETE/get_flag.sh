#!/bin/sh

wget -m "https://www.icec.ctf/"
grep -Ro "IceCTF{.*}"
