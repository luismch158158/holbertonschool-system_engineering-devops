#!/usr/bin/python3
"""Python script to export data in the JSON format records
all tasks from all employees"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    base_url = "https://jsonplaceholder.typicode.com/users"
    users_members = requests.get(base_url).json()

    with open('./todo_all_employees.json', 'w', encoding="UTF-8") as f:
        obj = {}

        for usr_info in users_members:
            new_list = []
            id = usr_info.get("id")
            todo_user = requests.get("{:s}/{:d}/todos".format(
                base_url, id)).json()
            username = usr_info.get("username")
            for task_usr in todo_user:
                task_title = task_usr.get("title")
                task_completed_status = task_usr.get("completed")
                new_obj = {
                    "username": username,
                    "task": task_title,
                    "completed": task_completed_status,
                }
                new_list.append(new_obj)
            obj[id] = new_list
        json.dump(obj, f, indent=4)
