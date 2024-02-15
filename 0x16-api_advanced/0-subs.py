#!/usr/bin/python3
"""Function to query subscribers (total subscribers) for a given subreddit"""
import requests

# Function definition to get the number of subscribers for a given subreddit
def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    
    # Construct the URL to retrieve subreddit information in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define headers for the HTTP request, including a User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/tonyrealzy)"
    }
    
    # Send an HTTP GET request to the specified URL with the provided headers
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status code indicates success
    if response.status_code == 200:      
        # Parse the JSON response and extract the "data" section
        data = response.json().get("data")
        
        # Return the number of subscribers from the "subscribers" key in the "data" section
        return data.get("subscribers")
    
    return 0
