#!/usr/bin/env python3

import pickle
import base64
import sys

class beet:
    def __init__(self, name):
        self.name = name

print("welcome to my beet reciever! i'm on a quest to find the best beets in the world\nsend me your beet when ready")
pickled_beet = base64.b64decode(raw_input())
beet = pickle.loads(pickled_beet)
print("thanks for your beet! " + str(beet.name) + " sounds like it is delicious!")
sys.exit(0)


