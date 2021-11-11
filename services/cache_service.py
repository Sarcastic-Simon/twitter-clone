from typing import List

from models.tweet import Tweet


class CacheService:
    def __init__(self) -> None:
        self.cache = []

    def store_tweet(self, tweet: Tweet) -> None:
        self.cache.append(tweet)

    def store_tweets(self, tweets: List[Tweet]) -> None:
        for tweet in tweets:
            self.cache.append(tweet)

    def load_tweets(self) -> List[Tweet]:
        return self.cache
