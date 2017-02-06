#!/bin/sh


tar xvf 983179bdb58ea980ec1fe7c45f63571d49b140bdd629f234be9c00a6edd8a4a7/layer.tar > /dev/null
strings ./bin/cat | tail -n 1|rev|cut -d " " -f1|rev

