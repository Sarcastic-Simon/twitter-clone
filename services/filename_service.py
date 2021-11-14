from os.path import join

from config.constants import tweets_folder, filename_pattern, users_folder
from models.tweet import Tweet
from models.user import User


def tweet_load_path(filename: str) -> str:
    return join(tweets_folder, filename)


def tweet_store_path(tweet: Tweet) -> str:
    name = _tweet_filename(tweet)
    path = join(tweets_folder, name)
    return path + '.json'


def _tweet_filename(tweet: Tweet) -> str:
    return tweet.date_published.strftime(filename_pattern)


def user_load_path(username: str) -> str:
    path = join(users_folder, username)
    return path + '.json'


def user_store_path(user: User) -> str:
    return join(users_folder, user.username) + '.json'
