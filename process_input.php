<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
// Sanitize and retrieve user input
$search_url = $_POST["search_url"];
$search_query = $_POST["search_query"];

// Construct the command to execute input.py
// $command = "C:/Users/Dell/AppData/Local/Programs/Python/Python311/python C:/xampp/htdocs/crawler/input.py -u {$search_url} -q {$search_query}";
$command = "python pyapp/input.py -u {$search_url} -q {$search_query}";
// Execute the command and capture the output
$output = exec($command);

// Redirect to the search result page after processing the input
header("Location: search_result.php");
exit;
}
?>