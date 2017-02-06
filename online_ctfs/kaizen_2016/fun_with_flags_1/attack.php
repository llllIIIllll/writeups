#!/usr/bin/php7.0

<?php



	$data = array('username' => '',
				  'password' => '' );

	echo(base64_encode(gzcompress(serialize($data))));

?>