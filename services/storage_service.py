from os import listdir
from os.path import exists
from typing import List, Optional

from jsonpickle import encode, decode

from config.constants import tweets_folder
from models.tweet import Tweet
from models.user import User
from services.filename_service import tweet_store_path, tweet_load_path, \
    user_store_path, user_load_path


def store_tweet_on_disk(tweet: Tweet) -> None:
    path = tweet_store_path(tweet)
    with open(path, 'w') as file:
        encoded = encode(tweet)
        file.write(encoded)


def load_tweets_from_disk() -> List[Tweet]:
    result = []
    for filename in listdir(tweets_folder):
        path = tweet_load_path(filename)
        with open(path, 'r') as file:
            tweet = decode(file.read())
            result.append(tweet)
    return result


def store_user_on_disk(user: User) -> None:
    path = user_store_path(user)
    with open(path, 'w') as file:
        encoded = encode(user)
        file.write(encoded)


def load_user_from_disk(username: str) -> Optional[User]:
    path = user_load_path(username)
    if not exists(path):
        return None
    with open(path, 'r') as file:
        decoded = decode(file.read())
        return decoded
