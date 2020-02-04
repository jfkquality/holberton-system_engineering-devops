#!/usr/bin/python3
"""Get completed tasks for user id."""
import requests
import json
from sys import argv


if __name__ == "__main__":
    """"Get completed tasks for user id."""
    userid = int(argv[1])
    payload = {'id': userid}
    url1 = 'https://jsonplaceholder.typicode.com/users/'
    r_user = requests.get(url1, params=payload)
    user = json.loads(r_user.text)  # or  r_user.json()
    print("USER NAME IS:", user[0]["name"])
    payload = {'userId': userid}
    url2 = 'https://jsonplaceholder.typicode.com/users/user["id"]/todos'
    r_todos = requests.get(url2, params=payload)
    todos = r_todos.json()
    total = len(todos[0])
    complete = 0
    completed = []
    for todo in todos:
        if todo["completed"]:
            completed.append(todo["title"])
            complete += 1
    print("Employee {} is done with tasks({}/{}):".format(user[0]["name"],
                                                          complete, total))
    for done in completed:
        print("\t {}".format(done))
