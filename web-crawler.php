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
    <link rel="stylesheet" href="css/index.css" />
    <link rel="stylesheet" href="css/web-crawler.css" />
    <link rel="icon" href="image/favicon.png" type="image/png" />
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
    </header>
    <!-- <hr /> -->
    <div class="boldline"></div>
    <!-- Welcome Banner Starts Here -->
    <div class="banner-txt banner">
      <h2>Provide us with your input</h2>
      <p>Enter your search url and search query in the box below:</p>
    </div>
    <section class="web-search">
      <form action="process_input.php" method="post">
        <div class="input-container">
          <h3 class="head1">Search URL</h3>
          <input
            type="url"
            name="search_url"
            placeholder="Enter your search url..."
            required
          />
        </div>
        <div class="input-container">
          <h3 class="head2">Search Query</h3>
          <input
            type="search"
            name="search_query"
            placeholder="Enter your search query..."
            required
          />
        </div>

        <input
          type="submit"
          name="submit"
          value="Web Crawl"
          class="btn btn-primary"
        />
      </form>
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
          <a href="index.php" target="_blank">HWC.LTD</a> All Rights Reserved.
        </p>
      </div>
    </section>
    <!-- footer Section Ends Here -->
  </body>
</html>
