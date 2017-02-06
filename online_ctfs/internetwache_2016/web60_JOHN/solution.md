

Operate under assumption the webpage is likely using `preg_replace` to make the regex replacement.

If you supply a //e option to the regular expression, you can _execute_ whatever becomes replaced. Total remote code execution.

So, if we search for: 
`/^(.*)/` which is anything
and we replace with a function call in PHP, supply anything for content,
we can execute a function.

Poking around with this, it seems like `system`, `exec`, `popen` and `passthru` (all usual system calls for PHP) are filtered by "Blacklisted keywords!"

_But,_ the backticks can go through. So I ran

`/^(.*)/e`, ``ls``, and `anything`. That got me directory listing, so I then ran

`/^(.*)/e`, ``cat flag.php``, and `anything`.

Got the result:

<?php
 
$FLAG = "IW{R3Pl4c3_N0t_S4F3}";

?>