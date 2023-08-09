# search.py

import csv
import mysql.connector
import sys
from collections import Counter


def fetch_data_from_mysql(db_config):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT title, url, text_content FROM your_table_name")
        data = cursor.fetchall()
        connection.close()
        return data
    except mysql.connector.Error as err:
        print("Error connecting to MySQL database:", err)
        return None

def fetch_data_from_csv(csv_file):
    try:
        with open(csv_file, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            data = [row for row in reader]
        return data
    except Exception as e:
        print("Error fetching data from CSV:", e)
        return None

def fetch_data():
    # If you are using a MySQL database to store data
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "crawler"
    }

    data = fetch_data_from_mysql(db_config)
    if data is None:
        # If MySQL data not available, try fetching from CSV
        data = fetch_data_from_csv("./datas/crawled_data.csv")

    return data



def calculate_relevance_score(search_query, text_content):
    # Convert both the search query and text content to lowercase for case-insensitive matching
    search_query = search_query.lower()
    text_content = text_content.lower()

    # Split the search query into individual words
    query_words = search_query.split()

    # Initialize a relevance score for each webpage to zero
    relevance_scores = {url: 0 for url in text_content.keys()}

    # Count the number of occurrences of each word in the search query within the text content
    for word in query_words:
        for url, content in text_content.items():
            relevance_scores[url] += content.count(word)

    return relevance_scores

def rank_results(relevance_scores):
    # Sort the webpages based on their relevance scores in descending order
    ranked_results = sorted(relevance_scores.items(), key=lambda x: x[1], reverse=True)

    return ranked_results



def save_search_results(search_results, csv_file):
    try:
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "URL", "Word Frequency"])
            for title, url, word_frequency in search_results:
                writer.writerow([url, title, word_frequency])
        print(f"Search results saved to {csv_file}.")
    except Exception as e:
        print("Error saving search results to CSV:", e)

def process_search_query(search_query):
    # Fetch data from database or CSV file
    data = fetch_data()

    # Implement the search engine logic here
    # For simplicity, let's just print the search query and data for now
    # print("Received search query:", search_query)
    # Implement the search engine logic here
    search_results = []
    processed_urls = set()
    
    for title, url, text_content in data:
        # Tokenize the text content and count the frequency of words
        text_tokens = text_content.split()
        word_frequency = Counter(text_tokens)

        # Check if the search query matches any word in the text content
        for query_word in search_query.split():
            if query_word in word_frequency:
                search_results.append((title, url, word_frequency[query_word]))

    # Sort the search results based on word frequency in descending order
    search_results.sort(key=lambda x: x[2], reverse=True)

    # "Fetched data:", data: This will print all the data fetched.
    # print("Fetched data:", data)
    # print("Fetched data: Confirmed")

    # Display the search results
    print(f"Search Results for '{search_query}':")
    for i, (title, url, _) in enumerate(search_results, start=1):
        print(f"{i}. Title: {url}")
        print(f"     URL: {title}")
        print()

    # Save the search results to the CSV file
        save_search_results(search_results, "./datas/search_results.csv")
        
# Get the search query from input.py
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please provide a search query.")
        sys.exit(1)

    search_query = sys.argv[1]
    process_search_query(search_query)
