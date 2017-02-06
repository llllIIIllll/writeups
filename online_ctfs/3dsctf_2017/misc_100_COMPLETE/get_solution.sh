#!/bin/bash

#
# Final QR code yields:
# QR-Code:Y0ur gift is in goo.gl/wFGwqO inugky3leb2gqzjanruw42yk
#
# Link yields flag:
#   3DS{I_h0p3_th4t_Y0u_d1d_n0t_h4v3_ch4ck3d_OnE_by_0n3}

function next(){
	echo `zbarimg $1 2>/dev/null|head -n 1|rev|cut -d " " -f1|rev`.png
}


NEXT="7ab7df3f4425f4c446ea4e5398da8847.png"
while [ 1 ]
do
	echo $NEXT
	NEXT=`next $NEXT`

done
