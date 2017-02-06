#!/bin/bash

echo "You can crack the given hash, "
echo " c7e83c01ed3ef54812673569b2d79c4e1f6554ffeb27706e98c067de9ab12d1a"
echo "online at http://md5decrypt.net/en/Sha256/"
echo " "
curl "http://kitty.vuln.icec.tf/login.php" --data "username=admin&password=Vo83*"|grep -o "IceCTF{.*}"
