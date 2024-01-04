#!/usr/bin/python3
""" script that return information about a user TODO list """


import requests
import sys


if __name__ == '__main__':

    user_id = int(sys.argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()
    user_tasks = []
    all_tasks = 0

    for task in tasks:
        if task['userId'] == user_id:
            all_tasks += 1
            if task['completed']:
                user_tasks.append(task['title'])

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    print('Employee {} is done with tasks({}/{}):'.format(user.json()['name'], len(user_tasks), all_tasks))

    for task in user_tasks:
        print('\t {}'.format(task))
