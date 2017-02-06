__web25 :: Mr. Robot__
===========================

> Disallow it!

-----------------------------------

This is a web challenge, and the challenge title is __Mr. Robot__ while the challenge prompt _Disallow it_... all of this hints to a [`robots.txt`][robots.txt]  file.

To validate my assumption, I went to the [URL]: `https://ctf.ekoparty.org/robots.txt`.

The page contained:

```
User-agent: *
Disallow: /static/wIMti7Z27b.txt
```

Aha! They are trying to hide something with the [`robots.txt`][robots.txt] file. Let's navigate to that location and see what it is they are keeping us.

I go to the [URL]...

```
EKO{robot_is_following_us}
```

__Aannnd we get our flag.__

You should take note of this kind of challenge; the [`robots.txt`][robots.txt] file is a classic web challenge.

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