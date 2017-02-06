<?php
/**
 *
 */
include('file_list.php');
?>
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0 Level 2//EN">
<html>
  <head>
    <title>Uploader</title>
  </head>
  <body>
    <h1>Simple Uploader</h1>
    <p>There are no upload features.</p>
    <h3>Files</h3>
    <table width="100%" border="1">
		  <tr>
			<th>#</th>
			<th>Filename</th>
			<th>Size</th>
			<th>Link</th>
		  </tr>
			  <?php foreach($files as $file): ?>
	<?php if($file[0]) continue; // visible flag ?>  
		  <tr>
			<td><?= $file[1]; ?></td>
			<td><?= $file[2]; ?></td>
			<td><?= $file[3]; ?> bytes</td>
			<td><a href="download.php?f=<?= $file[4]; ?>">Download</a></td>
		  </tr>
          <?php endforeach;?>
      </table>
  </body>
</html>
