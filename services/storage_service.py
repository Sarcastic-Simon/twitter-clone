from os import listdir
from os.path import exists
from typing import List, Union

from jsonpickle import encode, decode

from models.tweet import Tweet
from models.user import User
from services.filename_service import FilenameService


class StorageService:
    def __init__(self, filenames=FilenameService()) -> None:
        self.filenames = filenames

    def store_tweet(self, tweet: Tweet) -> None:
        path = self.filenames.tweet_store_path(tweet)
        with open(path, 'w') as file:
            encoded = encode(tweet)
            file.write(encoded)

    def load_tweets(self) -> List[Tweet]:
        result = []
        for filename in listdir(self.filenames.tweets()):
            path = self.filenames.tweet_load_path(filename)
            with open(path, 'r') as file:
                tweet = decode(file.read())
                result.append(tweet)
        return result

    def store_user(self, user: User) -> None:
        path = self.filenames.user_save_path(user)
        with open(path, 'w') as file:
            encoded = encode(user)
            file.write(encoded)

    def load_user(self, username: str) -> Union[User, None]:
        path = self.filenames.user_load_path(username)
        if not exists(path):
            return None
        with open(path, 'r') as file:
            decoded = decode(file.read())
            return decoded
