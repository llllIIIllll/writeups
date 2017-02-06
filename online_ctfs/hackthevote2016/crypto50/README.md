__crypto50 :: TOPKEK__
===========================

_John Hammond_ | _Sunday, November 6th, 2016_

> A CNN reporter had only one question that she couldn't get off her mind

>    Do we even know, who is this 4 CHAN???

> So she set out to find who this 400lb hacker is. During her investigation, she came across this cryptic message on some politically incorrect forum online, can you figure out what it means?

> [kek](kek.txt)

> author's irc nick: krx

-----------------------------------

The challenge prompt didn't seem too have _too_ much to do with the actual challenge (except for the [repeated clips](https://www.youtube.com/watch?v=kRcdmbC0HHs) probably referring to the repeated bit).

I downloaded the file, and we assumed that each `KEK` or `TOP` meant either a zero or a one, like for [binary]. The exclamation-points `!` we just kind of assumed would be a number indicating _how_ many ones or zeros were there, like a multiplier.

Here is the quick [Python] code I wrote to crank it out:

``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-11-05 12:15:29
# @Last Modified by:   john
# @Last Modified time: 2016-11-05 12:33:58


handle = open("kek.txt")
contents = handle.read()
handle.close()

import binascii

things = contents.split()
# print things

new = []
for thing in things:
    
    if "KEK" in thing:
        character = "0"
    else:
        character = "1"

    number = thing.count('!')
    new.append( character * number )

end = "".join(new)

print "".join([ chr(int(end[i:i+8],2)) for i in range(0,len(end), 8) ])
```

The flag is displayed as: __`flag{T0o0o0o0o0P______1m_h4V1nG_FuN_r1gHt_n0W_4R3_y0u_h4v1ng_fun______K3K!!!}`__

[CTF]: https://en.wikipedia.org/wiki/Capture_the_flag#Computer_security
[Cyberstakes]: https://cyberstakesonline.com/
[OverTheWire]: http://overthewire.org/
[ctftime.org]: http://ctftime.org
[SECCON 2015 Online CTF]: https://ctftime.org/event/274
[SECCON]: http://ctf.seccon.jp/
[32C3 CTF]: https://ctftime.org/event/278
[32C3]: https://32c3ctf.ccc.ac/
[EKOPARTY 2016 CTF]: https://ctftime.org/event/342
[robots.txt]: http://www.robotstxt.org/
[URL]: https://en.wikipedia.org/wiki/Uniform_Resource_Locator
[nikto]: http://sectools.org/tool/nikto/
[Netcraft]: https://www.netcraft.com/
[CSS]: https://en.wikipedia.org/wiki/Cascading_Style_Sheets
[Tor Browser]: https://www.torproject.org/projects/torbrowser.html.en
[Tor]: https://www.torproject.org/projects/torbrowser.html.en
[64-bit]: https://en.wikipedia.org/wiki/64-bit_computing
[Linux]: https://en.wikipedia.org/wiki/Linux
[HTML]: https://en.wikipedia.org/wiki/HTML
[Firefox]: https://www.mozilla.org/en-US/firefox/new/
[Chromium]: https://en.wikipedia.org/wiki/Chromium_(web_browser)
[Google]: https://www.google.com/
[Googled]: https://www.google.com/
[Googling]: https://www.google.com/
[Stack Overflow]: http://stackoverflow.com/
[Bootstrap]: http://getbootstrap.com/
[404]: https://en.wikipedia.org/wiki/HTTP_404
[nginx]: https://www.nginx.com/
[IRC]:https://en.wikipedia.org/wiki/Internet_Relay_Chat
[javascript]: https://en.wikipedia.org/wiki/JavaScript
[Firebug]: http://getfirebug.com/
[HTTP]: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
[GET]: http://www.w3schools.com/TAgs/ref_httpmethods.asp
[Content-Type]: https://www.w3.org/Protocols/rfc1341/4_Content-Type.html
[JPEG]: https://en.wikipedia.org/wiki/JPEG
[JPG]: https://en.wikipedia.org/wiki/JPEG
[CSS]: https://en.wikipedia.org/wiki/Cascading_Style_Sheets
[curl]: https://curl.haxx.se/
[RFC 5988]: https://tools.ietf.org/html/rfc5988
[PIL]: http://www.pythonware.com/products/pil/
[Python image Library]: http://www.pythonware.com/products/pil/
[Python imaging Library]: http://www.pythonware.com/products/pil/
[binary]: https://en.wikipedia.org/wiki/Binary_number
[Python]: https://www.python.org/