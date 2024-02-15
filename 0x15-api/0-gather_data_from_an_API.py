#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    # URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"
    # Get user information for the specified employee ID
    user = requests.get(url + "users/{}".format(sys.argv[1])).json() 
    # Get to-do list for the specified employee ID
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    # Extract titles of completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    # Print information about completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))   
    # Print the titles of completed tasks
    [print("\t {}".format(c)) for c in completed]
