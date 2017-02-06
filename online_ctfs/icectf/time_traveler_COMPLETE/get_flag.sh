#!/bin/bash

lynx --dump "https://web.archive.org/web/20160601212948/http://time-traveler.icec.tf/"|grep "IceCTF"|awk '{print $1}'
