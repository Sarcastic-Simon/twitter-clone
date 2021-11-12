from bcrypt import hashpw, gensalt


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = hashpw(password.encode(), gensalt())
