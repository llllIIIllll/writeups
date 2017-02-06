#!/usr/bin/php

<?php
	
	function arr_to_str($arr) {
	    $out = array();
	    foreach ($arr as $key => $val) {
	        $v = $val;
	        if ($v === true) {
	            $v = 'true';
	        }
	        if ($v === false) {
	            $v = 'false';
	        }
	        $out[] = $key . '=' . $v;
	    }
	    return join('&', $out);
	}

	function str_to_arr($str) {
	    $pairs = explode('&', $str);
	    $out = array();
	    foreach ($pairs as $value) {
	        $a = explode('=', $value);
	        if (count($a) != 2) {
	            throw new Exception('Malformed item!');
	        }
	        $val = $a[1];
	        if ($val === 'true') {
	            $val = true;
	        }
	        else if ($val === 'false') {
	            $val = false;
	        }
	        $out[$a[0]] = $val;
	    }
	    return $out;
	}

	$SECRET_KEY = 'AAAAAAAAAAAAAAAA';

	$sess = array('logged_in' => true, 'name' => 'John Doe');
    $sess_str = arr_to_str($sess);


    // $_COOKIE_session = 'logged_in%3Dtrue%26name%3DJohn+Doe';
    $_COOKIE_session = 'name%3DJohn+Doe%26&a%3Daaaaaaaaaaaaaaaaaaa';
    $_COOKIE_hash = '2cc207d867af2d2a55ff4141b6e3e8f2';


    $cookie = urldecode($_COOKIE_session);


    // $hash = 

    print_r($sess);
    echo("\n\n\$session_str = " . $sess_str);
    echo("\n\n\$_COOKIE['session'] = " . urlencode($sess_str));
    echo("\n\n\$_COOKIE['hash'] = " . md5($SECRET_KEY . $sess_str));
    echo("\n\n\$cookie = " . $cookie);
    echo("\n\nmd5(\$SECRET_KEY . \$cookie) == \$_COOKIE['hash']");
    echo("\n\n".md5("\$SECRET_KEY" . $cookie) . " == " . $_COOKIE_hash);

    // echo($)


?>