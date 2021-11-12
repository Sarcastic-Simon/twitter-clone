from typing import List

from models.tweet import Tweet
from services.cache_service import CacheService
from services.storage_service import StorageService


class TweetService:
    def __init__(self, cache_service=CacheService(),
                 storage_service=StorageService()) -> None:
        self.cache_service = cache_service
        self.storage_service = storage_service

    def save_tweet(self, tweet: Tweet) -> None:
        self.cache_service.store_tweet(tweet)
        self.storage_service.store_tweet(tweet)

    def get_all_tweets(self) -> List[Tweet]:
        if not self.cache_service.load_tweets():
            tweets = self.storage_service.load_tweets()
            self.cache_service.store_tweets(tweets)

        return self.cache_service.load_tweets()


tweet_service = TweetService()
