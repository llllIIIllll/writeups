Assume the webpage actually is a git repository



You can grab it's contents with GitTools "Dumper" 
(I found this by searching github for anything with Internetwache)
https://github.com/internetwache/GitTools

Poke around with the git repo. `git log` to see other commits.
Get to those other commits with `git checkout <SHA1 HASH>`. 

You can find the flag in `git checkout 26858023dc18a164af9bfb23919489ab2`
and `cat index.html`.
