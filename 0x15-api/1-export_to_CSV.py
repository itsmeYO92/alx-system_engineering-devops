#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users"
    url = "{}/{}".format(api_url, employee_id)

    response = requests.get(url)
    username = response.json().get('username')

    todos_url = url + "/todos"
    response = requests.get(todos_url)
    tasks = response.json()

    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, username, task.get('completed'),
                               task.get('title')))

