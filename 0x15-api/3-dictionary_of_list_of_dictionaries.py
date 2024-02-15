#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"
    try:
        # Fetch user information for all employees
        users = requests.get(url + "users").json()
    except requests.exceptions.RequestException as e:
        # Handle potential errors during API requests
        print(f"Error: {e}")
        exit(1)
    # Create a dictionary with user IDs as keys and a list of to-do items as values
    todo_data = {
        u.get("id"): [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos", params={"userId": u.get("id")}).json()
        ] for u in users
    }
    # Write the JSON data to a file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_data, jsonfile)
