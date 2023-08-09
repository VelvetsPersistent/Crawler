<?php 

    include ('constants.php'); 
    include ('login-check.php'); 


?>
<!DOCTYPE html>
<html>
  <head>
    <title>Hubble WebCrawler</title>
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
    />
    <link rel="icon" href="image/favicon.png" type="image/png" />
    <link rel="stylesheet" href="css/index.css" />
  </head>
  <body>
    <header>
      <h1>Hubble WebCrawler</h1>
      <!-- Navigation bar Starts Here -->
      <div class="menu text-center">
        <a href="index.php">Home</a>
        <a href="web-crawler.php">WebCrawler</a>
        <a href="logo.html">Logo</a>
        <a href="about-us.php">About Us</a>
        <div class="wrapper" style="display: inline-block; vertical-align: middle;">
        <ul>
          <li><a href="logout.php" class="btn1">Logout</a></li>
        </ul>
        </div>
      </div>
      <!-- Logout Section Starts -->
    <div class="menu text-center">
      
    </div>
    </header>
    <!-- <hr /> -->
    <div class="boldline"></div>
    <!-- Welcome Banner Starts Here -->
    <div class="banner-txt banner">
      <h2>"Data Empowered || Unleash Insights."</h2>
      <p>
        Empower your business with our advanced web crawling solutions for
        comprehensive data extraction and actionable insights.
      </p>
      <div class="banner-btn">
        <a href="contact.php"><span></span>Find Out</a>
        <a href="about-us.php"><span></span>Read More</a>
      </div>
    </div>
    <!-- <hr /> -->
    <div class="bold-line"></div>

    <!-- Product Showcase Starts Here -->
    <section class="categories">
      <div class="container">
        <h2 class="text-center">Our Products</h2>
        <a href="web-crawler.php">
          <div class="box-3 float-container">
            <img
              src="image/WebCrawler.jpg"
              alt="WebCrawler"
              class="img-responsive img-curve"
            />
            <h3 class="float-text text-color">Web Crawler</h3>
          </div>
        </a>
        <a href="logo.html">
          <div class="box-3 float-container">
            <img
              src="image/logo.JPG"
              alt="Logo"
              class="img-responsive img-curve"
            />
            <h3 class="float-text text-color">Logo Game</h3>
          </div>
        </a>
        <!-- <a href="logo.html">
          <div class="box-3 float-container">
            <img src="logo.JPG" alt="Logo" class="img-responsive img-curve" />
            <h3 class="float-text text-white">Logo Game</h3>
          </div>
        </a> -->

        <div class="clearfix"></div>
      </div>
    </section>
    <!-- <hr /> -->
    <div class="bold-line"></div>

    <!-- social Section Starts Here -->
    <section class="social">
      <div class="container text-center">
        <div class="social-links">
          <a href="https://www.facebook.com/" target="_blank">
            <i class="fa fa-facebook"></i
          ></a>
          <a href="https://www.instagram.com/" target="_blank">
            <i class="fa fa-instagram"></i
          ></a>
          <a href="https://www.twitter.com/" target="_blank">
            <i class="fa fa-twitter"></i
          ></a>
          <a href="https://www.youtube.com/" target="_blank">
            <i class="fa fa-youtube"></i
          ></a>
        </div>
      </div>
    </section>
    <!-- social Section Ends Here -->
    
    <!-- footer Section Starts Here -->
    <section class="footer">
      <div class="container text-center">
        <p>
          Copyright © 2079-2080
          <a href="login.php" target="_blank">HWC.LTD</a> All
          Rights Reserved.
        </p>
      </div>
    </section>
    <!-- footer Section Ends Here -->
  </body>
</html>
