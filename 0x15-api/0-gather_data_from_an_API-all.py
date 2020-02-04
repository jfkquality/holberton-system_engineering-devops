#!/usr/bin/python3
import requests
import json

if __name__ == "__main__":
    int total = 0, complete = 0, incomplete = 0, size = 0

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    users =  requests.get('https://jsonplaceholder.typicode.com/users')
    tasks_dict = json.loads(r)
    size = len(tasks_dict[0])

    for user in users:
        complete = 0
        total = 0
        utasks = requests.get('https://jsonplaceholder.typicode.com/users/user.id/todos')
        utasks_dict = json.loads(utasks)
        todos = len(utasks_dict[0])
        completed = []
        for task in utasks:
            if task.completed = True:
                complete += 1
                completed[complete] = task.title
            total += 1
        print("Employee {} is done with tasks({}/{} {}):".format(user.name, completed, total, todos))
        for done in completed:
            print("\t {}".format(done))
