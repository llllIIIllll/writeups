#!/bin/bash

curl "http://web.angstromctf.com:1338/admin_7de7b2fed84fd29656dff73bc98daef391b0480efdb0f2e3034e7598b5a412ce.html" 2>/dev/null|grep flag|rev|cut -d " " -f1 | rev|sed 's|</p>||g'
