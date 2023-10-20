from flask_login import UserMixin # ez kell a felhasználói fiókhoz

class User(UserMixin):
    def __init__(self, id, username, password, prefered_background='background_image.jpg'):
        self.id = id
        self.username = username
        self.password = password
        self.prefered_background = prefered_background

    @staticmethod
    def find_user_by_username(username, users_list):
        for user in users_list:
            if user.username == username:
                return user
        return None

    @staticmethod
    def find_user_by_id(id, users_list):
        for user in users_list:
            if user.id == id:
                return user
        return None