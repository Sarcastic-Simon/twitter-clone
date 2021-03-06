from typing import List

from models import Tweet, User
from services.cache_service import (store_tweet_in_cache,
                                    load_tweets_from_cache,
                                    store_tweets_in_cache)
from services.storage_service import (store_tweet_on_disk,
                                      load_tweets_from_disk)


def post_tweet(username: str, message: str) -> None:
    tweet = Tweet(username, message)
    store_tweet_in_cache(tweet)
    store_tweet_on_disk(tweet)


def get_user_tweets(user: User) -> List[Tweet]:
    return [tweet for tweet in _all_tweets()
            if tweet.author == user.username]


def get_other_tweets(user: User) -> List[Tweet]:
    return [tweet for tweet in _all_tweets()
            if tweet.author not in user.followers
            if tweet.author != user.username]


def get_follower_tweets(user: User) -> List[Tweet]:
    return [tweet for tweet in _all_tweets()
            if tweet.author in user.followers]


def _all_tweets() -> List[Tweet]:
    if not load_tweets_from_cache():
        tweets = load_tweets_from_disk()
        store_tweets_in_cache(tweets)
    return load_tweets_from_cache()
