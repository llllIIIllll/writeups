import hashlib
time = 1455994278
for s in range(-60,61):
    for cint in range(256):
        if hashlib.sha1(str(time + s) + ":" + chr(cint)).hexdigest() == "c51a8f7a25330b5f79fce357b6069b415151a24c":
            print chr(cint)#Time is 18:51:18, 051th day of 2016 +- 30 seconds
#1455994278