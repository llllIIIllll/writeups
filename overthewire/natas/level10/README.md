__Natas :: Level 10__
================


_Patrick Ledzian_ | _Monday, December 21st, 2015_ 


> There is no information for this level, intentionally.


----------


Start by using a web browser to navigate to the website `http://natas10.natas.labs.overthewire.org/`

```
Login: natas10

Password: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu 

```

Once again we are supplied with an input box and source code

![Image Broke](edit1.png)

By examining the source code it becomes apparent this problem is almost exactly like level9, however the `;` is one of the forbidden characters.

`$key` is still where your command will execute, however we can't terminate the grep that comes before it.

Instead of terminating it, lets use a [regular expression] (regex) to change the grep into something valuable to us.

submit the command `.* /etc/natas_webpass/natas10 #`

The difference between level9 and level 10 is the `.*`

The `.` means look for any character and the `*`means "that occurs 0 or more times"

This will look for any string beginning with the path `/etc/natas_webpass/natas10`

(Seriously, read the regex link)

Voilà out pops the flag

natas11: U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK




[regular expression]: http://www.thegeekstuff.com/2011/01/regular-expressions-in-grep-command/




