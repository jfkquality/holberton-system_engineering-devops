#!/usr/bin/python3
"""Get completed tasks for user id."""
import csv
import json
import requests
import socket
from sys import argv


if __name__ == "__main__":
    """"Get completed tasks for user id."""
    userid = int(argv[1])

    payload = {'id': userid}
    url1 = 'https://jsonplaceholder.typicode.com/users/'
    r_user = requests.get(url1, params=payload)
    user = r_user.json()  # or json.loads(r_user.text)

    payload = {'userId': userid}
    url2 = 'https://jsonplaceholder.typicode.com/users/1/todos'
    r_todos = requests.get(url2, params=payload)
    todos = r_todos.json()  # or json.loads(r_todos.text)
    # headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    # f.writerow(headers)

    completed = []
    for todo in todos:
        completed.append({"task": todo["title"],
                          "completed": todo["completed"],
                          "username": user[0]["username"]})
    jdata = {todo['userId']: completed}
    # jdata = json.dumps(jdata)
    with open(str(userid) + ".json", "w") as outfile:
        json.dump(jdata, outfile)
