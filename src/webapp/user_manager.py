import json
from .models import User

file_path = '/Users/robertlippai/Documents/SZFM-VerbVenture/src/webapp/static/test_users.json'

def load_users_from_file():
    with open(file_path, 'r') as file:
        users_data = json.load(file)

    users_list = []
    for user_data in users_data:
        user = User(user_data['id'], user_data['username'], user_data['password'])
        users_list.append(user)

    return users_list

def add_user_to_file(user):
    with open(file_path, 'r') as file:
        users_data = json.load(file)

    users_data.append({
        'id': user.id,
        'username': user.username,
        'password': user.password
    })

    with open(file_path, 'w') as file:
        json.dump(users_data, file, indent=4)