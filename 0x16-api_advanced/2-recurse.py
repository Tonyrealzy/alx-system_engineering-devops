#!/usr/bin/python3
"""Function to query a list of the titles of all hot
articles on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of titles of all hot posts on a given subreddit."""

    # Construct the URL for querying hot posts in JSON
    # format for the specified subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    
    # Define headers for the HTTP request, including a User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    # Define parameters for the request, including "after"(pagination),
    # "count" (number of posts), and "limit" (posts per request)
    params = {
        "after": after}
    # Send an HTTP GET request to the specified URL with the provided
    # headers and parameters
    data = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    # Check if the response status code is 200
    if data.status_code == 200:
        results = data.json().get("data")
        after = results.get("after")

        for entry in results.get("children"):
            hot_list.append(entry.get("data").get("title"))

        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list

    return None
