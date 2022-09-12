#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    import sys

    id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/users/"
    url_user = "{:s}{:d}".format(base_url, id)
    url_todos = "{:s}{:d}/todos".format(base_url, id)
    url_todos_true = "{:s}?completed=true".format(url_todos)

    response_user = requests.get(url_user).json()

    response_todos = requests.get(url_todos).json()
    long_response = len(response_todos)

    response_todos_true = requests.get(url_todos_true).json()
    long_response_true = len(response_todos_true)

    print("Employee {:s} is done with tasks({:d}/{:d}):".format(
          response_user.get("name"), long_response_true, long_response))
    for task_done in response_todos_true:
        print("\t {:s}".format(task_done.get("title")))
