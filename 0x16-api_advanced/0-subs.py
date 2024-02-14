#!/usr/bin/python3
"""Function to query subscribers(not active users, total subscribers) for a given subreddit"""
import requests

# Function definition to get the number of subscribers for a given subreddit
def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    
    # Construct the URL to retrieve subreddit information in JSON format
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Define headers for the HTTP request, including a User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    # Send an HTTP GET request to the specified URL with the provided headers
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status code is 404 (Not Found)
    if response.status_code == 404:
        return 0
    
    # Parse the JSON response and extract the "data" section
    outcome = response.json().get("data")
    
    # Return the number of subscribers from the "subscribers" key in the "data" section
    return outcome.get("subscribers")