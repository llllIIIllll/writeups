__misc50 :: Hidden Inside EKO __
===========================

> Find the hidden flag inside the EKO pixels!

-----------------------------------

This challenge didn't really offer a whole ton of guidance -- I figured it was referring to a picture or an image because of the "pixels," and it must be a specific EKO image. 

Honestly, I opened up the source and looking for any image. I found the logo, and the background image.

Initially I found the path of the background image by checking out their [CSS] stylesheets. [`https://ctf.ekoparty.org/static/img/background.png`](https://ctf.ekoparty.org/static/img/background.png)

If you take a look at the image, ... and seriously hunt for it ... you will find the flag in the top left corner.

![background](background.png)

The flag is found to be __`EKO{th3_fl4g}`__.


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