__web50 :: RFC 7230__
===========================

> Get just __basic__ information from this server. (ctf.ekoparty.org)

-----------------------------------

Another web challenge, this time just asking us to get some basic information -- do simple reconnaissance. 

To do simple reconnaissance for a web site, typically you throw it at some scanner tools. In this case, I tried [`nikto`][nikto].

It found the flag immediately.

```
$ nikto -h "https://ctf.ekoparty.org"
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          52.204.197.190
+ Target Hostname:    ctf.ekoparty.org
+ Target Port:        443
+ Start Time:         2016-10-31 16:24:18 (GMT-4)
---------------------------------------------------------------------------
+ Server: EKO{this_is_my_great_server}
+ The anti-clickjacking X-Frame-Options header is not present.
```

Another friend found the flag by throwing it at [Netcraft].

The flag was found to be __`EKO{this_is_my_great_server}`__


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