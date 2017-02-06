__Natas :: Level 3__
================


_Patrick Ledzian_ | _Thursday, December 10th, 2015_ 


> There is no information for this level, intentionally.


----------


Start by using a web browser to navigate to the website `http://natas3.natas.labs.overthewire.org/`

```
Login: natas3

Password: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14

```
When you login you will be greeted by the banner "There is nothing on this page"

`ctrl + u` to see the html code and we see in the comments 

<!-- No more information leaks!! Not even Google will find it this time... -->

This is a major hint!

There is a way for websites to hide certain URL paths from search engine results

They use a file called [robots.txt]

Navigate to the URL `http://natas3.natas.labs.overthewire.org/robots.txt`

You will see the path that has been disallowed `/s3cr3t/`

Navigate to `http://natas3.natas.labs.overthewire.org/s3cr3t/`

![Image Broke](edit1.png)

Here we see another users.txt file, open that and find the key!

natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ


[robots.txt]: http://www.robotstxt.org/robotstxt.html
