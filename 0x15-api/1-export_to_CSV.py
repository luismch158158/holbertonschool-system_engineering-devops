#!/usr/bin/python3
"""script to export data in the CSV format."""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/users/"
    url_user = "{:s}{:d}".format(base_url, id)
    url_todos = "{:s}{:d}/todos".format(base_url, id)

    response_user = requests.get(url_user).json()

    response_todos = requests.get(url_todos).json()

    with open('./{}.csv'.format(id), 'w', encoding="UTF-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for member in response_todos:
            user_id = id
            username = response_user.get("username")
            task_completed_status = member.get("completed")
            task_title = member.get("title")
            final_array = [user_id, username, task_completed_status,
                           task_title]
            writer.writerow(final_array)
