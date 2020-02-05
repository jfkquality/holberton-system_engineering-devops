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
    user = json.loads(r_user.text)  # or  r_user.json()

    payload = {'userId': userid}
    url2 = 'https://jsonplaceholder.typicode.com/users/1/todos'
    r_todos = requests.get(url2, params=payload)
    # todos = json.loads(r_todos.text)  # or r_todos.json()
    todos = r_todos.json()
    # fname = todo['userID'] + '.csv'
    f = csv.writer(open(str(userid) + ".csv", "w"), quoting=csv.QUOTE_ALL)
    # headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    # f.writerow(headers)

    total = 0
    complete = 0
    completed = []

    for todo in todos:
        f.writerow([todo['userId'],
                    user[0]['username'],
                    todo['completed'],
                    todo['title']])
