#!/bin/bash

strings ws1_2.pcapng |grep -oE "BITSCTF{.*}" --color=never