from typing import List

from models.tweet import Tweet
from models.user import User
from services.cache_service import (store_tweet_in_cache,
                                    load_tweets_from_cache,
                                    store_tweets_in_cache)
from services.storage_service import store_tweet_on_disk, load_tweets_from_disk


def save_tweet(tweet: Tweet) -> None:
    store_tweet_in_cache(tweet)
    store_tweet_on_disk(tweet)


def get_all_tweets(user: User = None) -> List[Tweet]:
    if not load_tweets_from_cache():
        tweets = load_tweets_from_disk()
        store_tweets_in_cache(tweets)

    tweets = load_tweets_from_cache()
    if user is not None:
        tweets = [tweet for tweet in tweets
                  if tweet.author not in user.followers
                  if tweet.author != user.username]
    return tweets


def get_follower_tweets(user: User) -> List[Tweet]:
    if user is None:
        return []
    tweets = get_all_tweets()
    return [tweet for tweet in tweets if tweet.author in user.followers]


def get_my_tweets(user: User) -> List[Tweet]:
    if user is None:
        return []
    tweets = get_all_tweets()
    return [tweet for tweet in tweets if tweet.author == user.username]
