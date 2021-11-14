from typing import List

from models.tweet import Tweet
from models.user import User

_tweets = []
_users = {}


def store_tweet_in_cache(tweet: Tweet) -> None:
    _tweets.append(tweet)


def store_tweets_in_cache(tweets: List[Tweet]) -> None:
    for tweet in tweets:
        _tweets.append(tweet)


def load_tweets_from_cache() -> List[Tweet]:
    return _tweets


def store_user_in_cache(user: User) -> None:
    _users[user.username] = user


def load_user_from_cache(username: str) -> User:
    return _users.get(username)
