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
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/tonyrealzy)"
    }
    
    # Define parameters for the request, limiting the response to 10 posts
    params = {
        "limit": 10
    }
    
    # Send an HTTP GET request to the specified URL with the provided headers and parameters
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the response status code is 404 (Not Found)
    if response.status_code == 404:
        print("None")
        return
    
    # Parse the JSON response and extract the "data" section
    results = response.json().get("data")
    
    # Print the titles of the 10 hottest posts
    [print(child.get("data").get("title")) for child in results.get("children")]
