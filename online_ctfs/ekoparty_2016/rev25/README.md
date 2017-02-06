__rev25 :: JVM__
===========================

> Bytecodes everywhere, reverse them.
> 
> Attachment
> [rev25_3100aa76fca4432f.zip](rev25_3100aa76fca4432f.zip)

-----------------------------------

A reversing challenge. I assume with [Java], considering the title of the challenge is __JVM__.

I downloaded the [zip archive] attachment and unzipped it with the [`unzip`][unzip] command. 

It gave me this `EKO.class` [class file]. Those contain [Java] bytecode, and can typically be "[decompiled]" very easily. I did it with the online [Show My Code] tool. 

This what I was able to decode: 

``` java
public class EKO { 

    public EKO() {} 

    public static void main(string args[]) {
    
        int i = 0; 
        for(int j = 0; j < 1337; j++) 
            i += j; 


        string s = (new StringBuilder()).append("EKO{").append(i).append("}").toString(); 
    } 
}
```

Hmm. It looks like it builds a string with a certain number, which is the sum of all the numbers from `1` to `1337` (visble in the `for` loop).

I got this number really quickly in [Python]:

``` python
>>> sum( range(1337) )
893116
```

Sweet. That, concatenated with the flag format, should be our flag: __`EKO{893116}`__



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
[HTTPS]: https://en.wikipedia.org/wiki/HTTPS
[Java]: https://www.java.com/en/
[zip file]: https://en.wikipedia.org/wiki/Zip_(file_format)
[zip]: https://en.wikipedia.org/wiki/Zip_(file_format)
[zip archive]: https://en.wikipedia.org/wiki/Zip_(file_format)
[unzip]: https://linux.die.net/man/1/unzip
[class file]: https://en.wikipedia.org/wiki/Java_class_file
[Java class file]: https://en.wikipedia.org/wiki/Java_class_file
[decompile]: https://en.wikipedia.org/wiki/Decompiler
[decompiler]: https://en.wikipedia.org/wiki/Decompiler
[decompiled]: https://en.wikipedia.org/wiki/Decompiler
[Show My Code]: http://www.showmycode.com/
[ShowMyCode]: http://www.showmycode.com/
[Python]: https://www.python.org/