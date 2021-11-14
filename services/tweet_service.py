from typing import List

from models.tweet import Tweet
from services.cache_service import store_tweet_in_cache, \
    load_tweets_from_cache, store_tweets_in_cache
from services.storage_service import store_tweet_on_disk, load_tweets_from_disk


def save_tweet(tweet: Tweet) -> None:
    store_tweet_in_cache(tweet)
    store_tweet_on_disk(tweet)


def get_all_tweets() -> List[Tweet]:
    if not load_tweets_from_cache():
        tweets = load_tweets_from_disk()
        store_tweets_in_cache(tweets)

    return load_tweets_from_cache()
