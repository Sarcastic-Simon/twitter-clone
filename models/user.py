from werkzeug.security import generate_password_hash


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = generate_password_hash(password)
        self.followers = set()

    def __str__(self) -> str:
        return self.username

    def __repr__(self):
        return self.__str__()
