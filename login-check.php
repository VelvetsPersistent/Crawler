<?php 
       //Authorization - Ac
       
       //check whether the user is logged in or not
       if(!isset($_SESSION['user']))// IF user session is not set
    
       {
           //user not available and redirect to the login page
           $_SESSION['no-login-message'] = "<div class='error text-center btn'>Please Login to access<br> Hubble WebCrawler.</div>";
           header('location:'.SITEURL.'login.php');
       }
?>