from datetime import datetime


class Tweet:
    def __init__(self, author: str, message: str):
        self.author = author
        self.message = message
        self.date_published = datetime.utcnow()
