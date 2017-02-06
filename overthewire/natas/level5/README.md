__Natas :: Level 5__
================


_Patrick Ledzian_ | _Thursday, December 10th, 2015_ 


> There is no information for this level, intentionally.


----------


Start by using a web browser to navigate to the website `http://natas5.natas.labs.overthewire.org/`

```
Login: natas5

Password: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

```

Load the page and you will see "Access disallowed. You are not logged in"

`ctrl + u` to look at the html source

You see that there is nothing of interest in the source code, it even says so in the comments

Let us examine the packets being sent using Burp Suite, the same technique as level 4

Open Burp, set the proxy in Firefox to manual --> port 8080 (this should be default)

Make sure Burp intercept is on and refresh the natas5 page (if you need help doing any of this check out the natas level4 writeup)

![Image Broke](edit1.png)

Under that heading Params you will see that the cookie `loggedin --> 0` change the 0 to a 1 and foward the packet

The page should change giving you the password for natas6!

`Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1`
