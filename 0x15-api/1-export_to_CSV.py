#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
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
    # Open a CSV file for writing
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write header row to CSV file
        writer.writerow(["User ID", "Username", "Completed", "Title"])
        # Write each to-do item as a row in the CSV file
        for todo in todos:
            writer.writerow([user_id, username,
                             todo.get("completed"), todo.get("title")])

