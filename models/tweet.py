from datetime import datetime


class Tweet:
    def __init__(self, author: str, message: str) -> None:
        self.author = author
        self.message = message
        self.date_published = datetime.utcnow()

    def __str__(self) -> str:
        return f"{self.author} - {self.date_published} - {self.message}"

    def __repr__(self) -> str:
        return self.__str__()
