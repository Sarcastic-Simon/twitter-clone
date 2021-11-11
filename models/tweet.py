from datetime import datetime


class Tweet:
    def __init__(self, author, message):
        self.author = author
        self.message = message
        self.date_published = datetime.utcnow()

    def __str__(self):
        return f"{self.author} - {self.date_published} - {self.message}"

    def __repr__(self):
        return self.__str__()
