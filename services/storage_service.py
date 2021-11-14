from os import listdir
from os.path import exists
from typing import List, Optional

from jsonpickle import encode, decode

from models.tweet import Tweet
from models.user import User
from services.filename_service import filename_service


class StorageService:
    def store_tweet(self, tweet: Tweet) -> None:
        path = filename_service.tweet_store_path(tweet)
        with open(path, 'w') as file:
            encoded = encode(tweet)
            file.write(encoded)

    def load_tweets(self) -> List[Tweet]:
        result = []
        for filename in listdir(filename_service.tweets()):
            path = filename_service.tweet_load_path(filename)
            with open(path, 'r') as file:
                tweet = decode(file.read())
                result.append(tweet)
        return result

    def store_user(self, user: User) -> None:
        path = filename_service.user_store_path(user)
        with open(path, 'w') as file:
            encoded = encode(user)
            file.write(encoded)

    def load_user(self, username: str) -> Optional[User]:
        path = filename_service.user_load_path(username)
        if not exists(path):
            return None
        with open(path, 'r') as file:
            decoded = decode(file.read())
            return decoded


storage_service = StorageService()
