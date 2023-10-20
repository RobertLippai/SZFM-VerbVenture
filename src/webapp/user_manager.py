import json
from .models import User

file_path = '/Users/robertlippai/Documents/SZFM-VerbVenture/src/webapp/static/test_users.json'

def load_users_from_file():
    with open(file_path, 'r') as file:
        users_data = json.load(file)

    users_list = []
    for user_data in users_data:
        user = User(user_data['id'], user_data['username'], user_data['password'], user_data.get('prefered_background', ''))
        users_list.append(user)

    return users_list

def add_user_to_file(user):
    with open(file_path, 'r') as file:
        users_data = json.load(file)

    users_data.append({
        'id': user.id,
        'username': user.username,
        'password': user.password,
        'prefered_background': user.prefered_background
    })

    with open(file_path, 'w') as file:
        json.dump(users_data, file, indent=4)

def update_preferred_background(username, prefered_background):
    # Find the user by username and update the preferred_background field
    users_list = load_users_from_file()

    for user in users_list:
        if user.username == username:
            user.prefered_background = prefered_background
            print("found")
            break

    for user in users_list:
        print(user.username)

    # Save the updated users list back to the JSON file
    with open(file_path, 'w') as file:
        users_data = [{
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'prefered_background': user.prefered_background  # Add the prefrred_background field
        } for user in users_list]
        json.dump(users_data, file, indent=4)
