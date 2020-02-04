#!/usr/bin/python3
import requests
import json
from sys import argv

if __name__ == "__main__":

    userid = int(argv[1])
    # tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    payload = {'id': userid}
    r_user =  requests.get('https://jsonplaceholder.typicode.com/users/', params=payload)
    user = json.loads(r_user.text)  # or  r_user.json()
    print("USER NAME IS:", user[0]["name"])
    payload = {'userId': userid}
    r_todos = requests.get('https://jsonplaceholder.typicode.com/users/user["id"]/todos', params=payload)
    todos = r_todos.json()
    total = len(todos[0])
    complete = 0
    completed = []
    for todo in todos:
        if todo["completed"]:
            completed.append(todo["title"])
            complete += 1
    print("Employee {} is done with tasks({}/{}):".format(user[0]["name"], complete, total))
    for done in completed:
        print("\t {}".format(done))
