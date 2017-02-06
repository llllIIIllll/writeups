Google CTF 2016 :: Ernst Echidna
================================

> Can you hack this website? The robots.txt sure looks interesting.

---------------------------

___John Hammond | April 29th, 2016___

As it says in the challenge prompt, the best place to start here is in the website's `robots.txt`.

```
Disallow: /admin 
```

It notes that any search engine cannot access the `/admin` page. Well that must be an interesting page, then, let's check that out!

![The admin pages tells us we are not logged in!](initial_admin.png)

```
You are not logged in!
```

Welp, it yells at us because we aren't logged in. Okay then, can we log in?

![The webpage](webpage.png)

Back at the original page, it tells us we can register. Let's try that.

It's a simple username and password form. I just entered the letter `a` as my username and then `b` as my password.

![Registering...](register.png)

It seemed to let me in... but will that `/admin` page? I navigated back to it.

![It says, "Sorry, this interface is restricted to administrators only"](restricted.png)

```
Sorry, this interface is restricted to administrators only
```

Oh, great, we're not able to access it because we're not an admin. That's annoying -- but it makes sense. So now what do we do?

Well I reached for the low-hanging fruits and tried to check out my cookies. I did this with [Firefox]'s extension called [Cookie Manager+]. I was able to find the cookie that was set from this site, and it was called `md5-hash`.

![Cookie Manager+...](cookie_manager.png)

It looks like the cookie has its value set to `0cc175b9c0f1b6a831c399e269772661`, supposedly an [MD5] hash. [MD5] is known to be pretty easy to crack, so... can we crack it?

I tried it with some cheeky online tool, [md5cracker.org][http://md5cracker.org/]. 

![md5cracker found it be `a`!](md5cracker.png)

Oh woah! It's just the letter `a`... what I put my username to be! Is that all it is doing to validate?

I wonder if we can _trick_ it to think that I am the administrator just by using `admin` as my username. I tried that with the login... but it really didn't like that.

![](no_admin.png)

```
'admin' account already taken!
```

But wait, can't we just change our cookie value? Let's just [MD5] hash the value `admin`, and then see if it will let us access that `/admin` page!

I did this with the same online tool [md5cracker.org][http://md5cracker.org/] and got the hash: `21232f297a57a5a743894a0e4a801fc3`

![](hash_admin.png)

Now with [Cookie Manager+] we can set that as our cookie.

![](cookie_edit.png)

Sweet. Now, can we access that `/admin` page...?

![](flag.png)

Heck yeah we can! Looks like we got our flag!

__The flag is: `CTF{renaming-a-bunch-of-levels-sure-is-annoying}`__
