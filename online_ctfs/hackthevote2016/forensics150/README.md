__forensics150 :: Warpspeed__
===========================

_John Hammond_ | _Sunday, November 6th, 2016_

> Our Trump advertising campaign is incredible, it's skyrocketing! It's astronomical! Wait stop!! SLOW DOWN!!!
> [warp_speed](warp_speed.jpg)
> author's irc nick: krx

-----------------------------------

The [image](warp_speed.jpg) provided in the challenge prompt contains the flag; it is just a matter of patching it up in a way we can actually read it. I used [PIL], the [Python Imaging Library] to reverse manipulations to the image. 

Two effects had to be undone:
1) a "roll" effect to the image that offsets each row (`8` pixels high) by 8 pixels to the left each row.
2) a "shuffled card effect". The un-"rolled" image reveals two side by side _stacks_ of strips (`8`pix*`500`pix) which need to be shuffled together in alternating order.

The following is the script used to fix the image:

``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-11-06 00:48:35
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-11-06 19:05:50

from PIL import Image

image = Image.open("warp_speed.jpg")

row_height = 8
number_rows = 32
side_size = 500

image_total_width = 1000

for i in range(number_rows):

    region = image.crop( (  0, row_height*i, 
                            image_total_width, row_height*(i+1) ) )

    image.paste(region, ( -(row_height*i), row_height*i, 
                            image_total_width - ( row_height*i ), row_height*(i+1) ))

image2 = Image.new( 'RGBA', (side_size,side_size) )

first_half = True

i = 0
Q = 0
while ( i < number_rows * 2 ):

    if first_half:
        region = image.crop( ( 0, row_height*i, side_size, row_height*(i+1) ) )
    else:
        region = image.crop( ( side_size, row_height*i, image_total_width, row_height*(i+1) ) )

        i += 1

    image2.paste( region, ((0, row_height*Q, side_size, row_height*(Q+1))) )

    Q += 1

    # Alternate sides
    first_half = not first_half

image2.show()
image2.save("winner.jpg")
```

Flag turns out to be: __`flag{1337_ph0t0_sk1ll5}`__

![winner.jpg](winner.jpg)

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