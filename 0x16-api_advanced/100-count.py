#!/usr/bin/python3
"""
A recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import json
import requests

def count_words(subreddit, word_list, after="", count=None):
    """Prints counts of given words."""

    # Initialize count list if it's the first call
    if count is None:
        count = [0] * len(word_list)

    # Construct the URL for querying hot articles in JSON format for the specified subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Send an HTTP GET request to the specified URL with the provided parameters
    response = requests.get(url, params={'after': after}, allow_redirects=False, headers={'user-agent': 'bhalut'})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Iterate through each article in the response
        for topic in data['data']['children']:
            # Split the title into words and check for matches with the given word_list
            for word in topic['data']['title'].split():
                for i, target_word in enumerate(word_list):
                    if target_word.lower() == word.lower():
                        count[i] += 1

        # Update the "after" parameter for pagination
        after = data['data']['after']

        # If there are no more articles, process and print the counts
        if after is None:
            save = []

            # Combine counts for identical words
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            # Sort and print counts
            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i].lower() > word_list[j].lower() and
                             count[j] == count[i])):
                        # Swap counts and words
                        count[i], count[j] = count[j], count[i]
                        word_list[i], word_list[j] = word_list[j], word_list[i]

            # Print non-zero counts
            for i in range(len(word_list)):
                if count[i] > 0 and i not in save:
                    print(f"{word_list[i].lower()}: {count[i]}")
        else:
            # If there are more articles, recursively call the function with updated parameters
            count_words(subreddit, word_list, after, count)

# Example usage:
subreddit_name = "python"
keywords_list = ["Python", "programming", "reddit"]
count_words(subreddit_name, keywords_list)
