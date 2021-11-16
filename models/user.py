from werkzeug.security import generate_password_hash


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = generate_password_hash(password)
        self.followers = set()
