#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    # Get the user ID from the command-line argument
    user_id = sys.argv[1]
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"
    try:
        # Fetch user information for the specified user ID
        user = requests.get(url + "users/{}".format(user_id)).json()
        # Extract username from user information
        username = user.get("username")
        # Fetch to-do list for the specified user ID
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
    except requests.exceptions.RequestException as e:
        # Handle potential errors during API requests
        print(f"Error: {e}")
        sys.exit(1)
        # Open a JSON file for writing
    with open("{}.json".format(user_id), "w") as jsonfile:
        # Create a dictionary with user ID as the key and a list of to-do items as the value
        json_data = {
            user_id: [
                {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username
                } for todo in todos
            ]
        }
        # Write the JSON data to the file
        json.dump(json_data, jsonfile)
