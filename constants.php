<?php
    //Start Session
    session_start();

//create constants to store non REPEATING values
define('SITEURL','http://localhost/crawler/');
define('LOCALHOST', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'crawler');



$conn = mysqli_connect(LOCALHOST, DB_USERNAME, DB_PASSWORD) or die(mysqli_error($conn)); //database connection
$db_select = mysqli_select_db($conn, DB_NAME)or die(mysqli_error($conn)); // selecting database


?>