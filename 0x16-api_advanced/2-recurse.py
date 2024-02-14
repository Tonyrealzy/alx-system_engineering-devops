#!/usr/bin/python3
"""Function to query a list of the titles of all hot articles on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    
    # Construct the URL for querying hot posts in JSON format for the specified subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    
    # Define headers for the HTTP request, including a User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/tonyrealzy)"
    }
    
    # Define parameters for the request, including "after" (pagination), "count" (number of posts), and "limit" (posts per request)
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    
    # Send an HTTP GET request to the specified URL with the provided headers and parameters
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the response status code is 404 (Not Found)
    if response.status_code == 404:
        return None
    
    # Parse the JSON response and extract the "data" section
    results = response.json().get("data")
    
    # Update the "after" parameter for pagination
    after = results.get("after")
    
    # Update the "count" parameter to keep track of the number of posts
    count += results.get("dist")
    
    # Iterate over the "children" in the JSON response and append titles to the hot_list
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    # If there are more posts (i.e., "after" is not None), recursively call the function with updated parameters
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    
    # If there are no more posts, return the final hot_list
    return hot_list
