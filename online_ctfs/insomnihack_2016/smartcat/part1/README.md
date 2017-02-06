__InsomniHack CTF :: SmartCat1__
================


_Caleb Stewart_ | _Sunday, January 17, 2016_ 


> Damn it, that stupid smart cat litter is broken again
> Now only the debug interface is available [`here`][smartcat]  and this stupid thing only permits one ping to be sent!
> I know my contract number is stored somewhere on that interface but I can't find it and this is the only available page! Please have a look and get this info for me !
> FYI No need to bruteforce anything there. If you do you'll be banned permanently


----------

![Smart Cat](../canihaz.jpg)

To start things off, we recognzied that the server was most likely appending whatever we typed to some ping command. With this in mind we started tring strings such as "localhost; ls", to see if we could get access to raw shell commands. We immediately saw that the server was checking for a list of special characters, and blocking offending input. We started trying all special characters, and ended up with this list: "&$`()|{} ". You'll notice that this is basically every useful special character known to man, except a few.

We noticed that the less than and greater than symbols weren't blocked, which are redirect symbols in bash. Therefore, we could redirect the output of ping to files in /tmp (where we had write permission), with strings like "localhost>/tmp/useless". This wasn't very helpful but was interest. We could also redirect files into ping, but ping doesn't read anything from standard input so this was also useless.

At this point, proceeded to bang our heads against the wall for a couple hours. In our mad scramble for answers, we found some "hints" in the HTTP headers of the page. They hints embedded in the "x-powered-by" HTTP header and were a random selection of the following:

```
solve_me_already
format-me-i-im-famous
mod_cassette_is_back/0.1
dirbuster.will.not.help.you
```

These hints weren't incredibly helpful. Obviously, "solve_me_already" was just mocking us. "format-me-i-im-famous" we thought was promising but could not find any useful formatting related exploits. "mod_cassette_is_back/0.1" led us to Haskell library. We then researched Haskell and its horrible syntax for around an hour to no end. In the end, the so called "hints" simply lead us in the wrong direction.

Out of dispair, we revisited the basic input box and restricted characters. While throwing things at the server, we realized we had never tried the new line character to separate commands. This allowed us to execute something after the ping by entering something like `localhost%0Als`. With that, we recieved a directory listing:

```
index.cgi
there
```

We were still restricted by the character filtering, therefore no parameters. We figured out we could read a file by called `cat` and redirecting a file to its standard input (`%0Acat</etc/passwd`). From here we still needed a filename, and we couldn't pass a parameter to ls. We decided to run `find`, which gave us a nice file tree from the current directory:

```
.
./index.cgi
./there
./there/is
./there/is/your
./there/is/your/flag
./there/is/your/flag/or
./there/is/your/flag/or/maybe
./there/is/your/flag/or/maybe/not
./there/is/your/flag/or/maybe/not/what
./there/is/your/flag/or/maybe/not/what/do
./there/is/your/flag/or/maybe/not/what/do/you
./there/is/your/flag/or/maybe/not/what/do/you/think
./there/is/your/flag/or/maybe/not/what/do/you/think/really
./there/is/your/flag/or/maybe/not/what/do/you/think/really/please
./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell
./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me
./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously
./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though
./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here
./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is
./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the
./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the/flag
```

We now had the file name, and we simply had to redirect that file into cat to grab the flag:

```
%0Acat<./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the/flag
```

And with that, we had the flag.

[smartcat]: http://smartcat.insomnihack.ch/cgi-bin/index.cgi