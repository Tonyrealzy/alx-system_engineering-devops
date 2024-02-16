#!/usr/bin/python3
"""Function to print the titles of the first 10 hot posts on a given Reddit subreddit."""
import requests

# Function definition to print the titles of the 10 hottest posts on a given subreddit
def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    
    # Construct the URL to retrieve the 10 hottest posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    
    # Define headers for the HTTP request, including a User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    # Send an HTTP GET request to the specified URL with the provided headers and parameters
    data = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status code is 200
    if data.status_code == 200:
        data = data.json().get("data").get("children")
        for element in data:
            print(element.get("data").get("title"))
    else:
        print(None)