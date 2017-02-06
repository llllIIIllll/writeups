import random
import ssl
import urllib2
import urllib
import re
import click



class SecurePrng(object):
    p = 4646704883L

    def __init__(self, x, y):
        # generate seed with 64 bits of entropy
        self.x = x
        self.y = y

    def next(self):
        self.x = (2 * self.x + 3) % self.p
        self.y = (3 * self.y + 9) % self.p
        return (self.x ^ self.y)



def HTTP(url, cookie=None, payload=None):
    if cookie:
        headers = { 'Cookie': 'session="%s"' % cookie }
    else:
        headers = {}

    if payload:
        payload = urllib.urlencode(payload)

    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    req = urllib2.Request(url, headers=headers, data=payload)
    # print (headers)
    # print (req.__dict__)
    return urllib2.urlopen(req, context=gcontext)



def get_cookie():
    req = HTTP('https://giant-goannas.ctfcompetition.com/start')
    s = req.headers.getheaders('Set-Cookie')[0]
    return re.findall('session="([^"]+).*', s)[0]


def submit_number(cookie, number):
    print "submit ", number
    req = HTTP('https://giant-goannas.ctfcompetition.com/lake', cookie=cookie, payload=dict(number=number))
    body = req.read()
    next_numbers = re.findall('([0-9]{4,})', body)
    print body
    if len(next_numbers) == 2:
        return False
    else:
        import ipdb
        ipdb.set_trace()
        return body


def try_to_guess(cookie):
    print "try to guess"
    req = HTTP('https://giant-goannas.ctfcompetition.com/lake', cookie=cookie)
    body = req.read()
    left, right = re.findall('([0-9]{4,})', body)
    req2 = HTTP('https://giant-goannas.ctfcompetition.com/lake', cookie=cookie, payload=dict(number=left))
    body2 = req2.read()
    next_numbers = re.findall('([0-9]{4,})', body2)
    if len(next_numbers) == 2:
        return int(left), [int(n) for n in next_numbers]
    else:
        return False, []

print "start the game"
try_to_play_id = 0

while 1:
    try_to_play_id += 1
    print "Our %d attemption" % try_to_play_id
    print "Let's get the cookie"
    cookie = get_cookie()
    print "Now, guess first number"
    number, possible_numbers = try_to_guess(cookie)
    if not number:
        continue
    print "Found", number, "and possible next numbers", possible_numbers

    if possible_numbers[0] > 1 * 1500 * 1000 * 1000 or possible_numbers[1] > 1 * 1500 * 1000 * 1000:
        print "but skip, we need only small variants"
        continue

    with click.progressbar(length=SecurePrng.p, label='Recovery prng state') as bar:
        for x in xrange(SecurePrng.p):
            y = number ^ x
            sprng = SecurePrng(x, y)
            value = sprng.next()
            if value in possible_numbers:
                break
            if x % 1000 == 0:
                bar.update(1000)
    print "Found", value, cookie, sprng.__dict__
    while 1:
        res = submit_number(cookie, value)
        if res:
            break
        value = sprng.next()
    print "Finish with", res
    break


