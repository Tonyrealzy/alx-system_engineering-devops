#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    # URL for the JSONPlaceholder API
    def fetch_todo_progress(employee_id):
        url = "https://jsonplaceholder.typicode.com/"
        # Get user information for the specified employee ID
        # Fetch employee information
        user_response = requests.get(f"{url}users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data.get("name")
        # Fetch TODO list for the employee
        todos_response = requests.get(f"{url}todos", params={"userId": employee_id})
        todos_data = todos_response.json()
        # Count completed tasks and total tasks
        completed_tasks = [task for task in todos_data if task.get("completed")]
        total_tasks = len(todos_data)

        # Display progress information
        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

        # Display titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task.get('title')}")
        if __name__ == "__main__":
            # Check if an employee ID is provided as a command-line argument
            if len(sys.argv) != 2:
                print("Usage: python script_name.py <employee_id>")
                sys.exit(1)

            # Parse the employee ID from the command-line argument
            employee_id = int(sys.argv[1])

            # Fetch and display TODO list progress for the given employee
            fetch_todo_progress(employee_id)
