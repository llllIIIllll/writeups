#!/usr/bin/env python

import binascii
import base64 as b

#print binascii.unhexlify("6236343a20615735305a584a755a58526659323975646d567963326c76626c3930623239736331397962324e72")

# This returns 'b64: aW50ZXJuZXRfY29udmVyc2lvbl90b29sc19yb2Nr'
print b.b64decode('aW50ZXJuZXRfY29udmVyc2lvbl90b29sc19yb2Nr')
