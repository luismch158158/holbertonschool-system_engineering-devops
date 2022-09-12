#!/usr/bin/python3
"""Python script to export data in the JSON format."""

if __name__ == "__main__":
    import json
    import requests
    import sys

    id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/users/"
    url_user = "{:s}{:d}".format(base_url, id)
    url_todos = "{:s}{:d}/todos".format(base_url, id)

    response_user = requests.get(url_user).json()

    response_todos = requests.get(url_todos).json()

    with open('./{}.json'.format(id), 'w', encoding="UTF-8") as f:
        obj = {
            id: [],
        }
        for member in response_todos:
            task_title = member.get("title")
            task_completed_status = member.get("completed")
            username = response_user.get("username")
            new_obj = {
                "task": task_title,
                "completed": task_completed_status,
                "username": username,
            }
            obj[id].append(new_obj)
        json.dump(obj, f, indent=4)
