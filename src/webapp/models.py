class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def find_user_by_username(username, users_list):
        for user in users_list:
            if user.username == username:
                return user
        return None
