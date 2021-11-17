from os.path import join

from config import (tweets_folder, filename_pattern, users_folder,
                    file_extension)
from models import Tweet, User


def tweet_load_path(filename: str) -> str:
    return join(tweets_folder, filename)


def tweet_store_path(tweet: Tweet) -> str:
    name = _tweet_filename(tweet)
    path = join(tweets_folder, name)
    return path + file_extension


def _tweet_filename(tweet: Tweet) -> str:
    return tweet.date_published.strftime(filename_pattern)


def user_load_path(username: str) -> str:
    path = join(users_folder, username)
    return path + file_extension


def user_store_path(user: User) -> str:
    return join(users_folder, user.username) + file_extension
