
class User:
    def __init__(self, user, username, password,profile_picture=None, admin=None):
        self.user = user
        self.username = username
        self.password = password
        self.profile_picture = profile_picture
        self.admin = admin


