import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import mysql.connector
import sys
import os


# Function to get all URLs from a given base URL
def get_all_urls(base_url):
    try:
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data - {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags (links) on the page
    links = soup.find_all('a')

    # Extract the URLs and titles from the links
    urls_titles = [(urljoin(base_url, link.get('href')), link.get_text()) for link in links]

    # Filter out None and empty URLs
    urls_titles = [(url, title) for url, title in urls_titles if url and not url.startswith('#')]

    return urls_titles

# Function to get text data from paragraph, h1, h2, h3, p, and span elements
def get_text_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data - {e}")
        return ""

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all paragraph, h1, h2, h3, and span elements
    elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'span'])

    # Extract the text content from the elements
    text_data = ", ".join(element.get_text(strip=True) for element in elements)

    return text_data

# Function to clean the text data
def clean_text_data(text_data):
    # Remove special characters and keep only alphabets
    cleaned_data = "".join(char if char.isalpha() else " " for char in text_data)

    # Remove extra spaces and convert to lowercase
    cleaned_data = " ".join(cleaned_data.split()).lower()

    return cleaned_data

# Main function to crawl and store the data
def crawl_and_store(base_url):
    # Get all URLs from the base URL
    urls_titles = get_all_urls(base_url)
    # Use the seed URL to create a table name in the MySQL database
    # seed_table_name = base_url.replace(".", "_").replace("/", "_").replace(":", "_")


    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crawler"
    )
    cursor = connection.cursor()

    # Create a table with the seed URL as the table name to store the data
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS crawled_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        url VARCHAR(255) NOT NULL,
        title VARCHAR(255) NOT NULL,
        text_content TEXT
    )
    """
    cursor.execute(create_table_query)

    # Create a CSV file to store the data
    # csv_file = open(f"{seed_table_name}_cleaned_data.csv", "w", newline="", encoding="utf-8")
    csv_file = open("./datas/crawled_data.csv", "w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["URL", "Title", "Cleaned Text Content"])


    # Crawl each URL and store the data
    for i, (url, title) in enumerate(urls_titles, 1):
        text_data = get_text_data(url)
        cleaned_data = clean_text_data(text_data)

        # Store the data in the MySQL database
        # insert_query = f"INSERT INTO {seed_table_name} (url, title, text_content) VALUES (%s, %s, %s)"
        insert_query = "INSERT INTO crawled_data (url, title, text_content) VALUES (%s, %s, %s)"
        data = (url, title, cleaned_data)
        cursor.execute(insert_query, data)

        # Store the data in the CSV file
        csv_writer.writerow([url, title, cleaned_data])

        print(f"{i}. URL: {url}")
        print(f"   Title: {title}")
        print(f"   Cleaned Text Content: {cleaned_data}\n")

    # Commit changes and close the database connection
    connection.commit()
    connection.close()

    # Close the CSV file
    csv_file.close()
    
    # Call search.py with the search query
    # os.system("python search.py")

# if __name__ == "__main__":
#     seed_url = print("Enter Seed URL as :python crawl.py https://example.com/")
#     crawl_and_store(seed_url)


# Get the seed URL from input.py
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python crawl.py <seed_url>")
        sys.exit(1)

    seed_url = sys.argv[1]
    crawl_and_store(seed_url)