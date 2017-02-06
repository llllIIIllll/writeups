#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-04-13 06:55:42
# @Last Modified by:   john
# @Last Modified time: 2016-04-13 06:56:40

import wave

w = wave.open('rain.wav')
for i in range(w.getnframes()):
    frame = w.readframes(i)
    print frame, 