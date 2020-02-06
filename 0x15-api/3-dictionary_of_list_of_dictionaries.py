#!/usr/bin/python3
"""Get completed tasks for user id."""
import csv
import json
import requests
import socket
from sys import argv


if __name__ == "__main__":
    """"Get completed tasks for user id."""
    # userid = int(argv[1])

    # payload = {'id': userid}
    url1 = 'https://jsonplaceholder.typicode.com/users/'
    # r_user = requests.get(url1, params=payload)
    r_user = requests.get(url1)
    users = r_user.json()  # or json.loads(r_user.text)

    jdata = {}
    jdata_all = {}
    for user in users:
        payload = {'userId': user['id']}
        url2 = 'https://jsonplaceholder.typicode.com/users/1/todos'
        r_todos = requests.get(url2, params=payload)
        # r_todos = requests.get(url2)
        todos = r_todos.json()  # or json.loads(r_todos.text)

        completed = []
        for todo in todos:
            completed.append({"task": todo["title"],
                              "completed": todo["completed"],
                              "username": user["username"]})
        jdata.update({todo["userId"]: completed})
        # jdata_all = jdata_all.update(jdata)
    # print(jdata)
    with open("todo_all_employees.json", "w") as outfile:
        json.dump(jdata, outfile)
