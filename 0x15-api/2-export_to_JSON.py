#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = "{}/{}".format(base_url, employee_id)

    response = requests.get(url)
    username = response.json().get('username')

    todos_url = url + "/todos"
    response = requests.get(todos_url)
    tasks = response.json()

    dictionary = {employee_id: []}
    for task in tasks:
        dictionary[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employee_id), 'w') as filename:
        json.dump(dictionary, filename)
