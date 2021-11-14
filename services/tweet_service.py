from typing import List

from models.tweet import Tweet
from services.cache_service import cache_service
from services.storage_service import storage_service


class TweetService:
    def save_tweet(self, tweet: Tweet) -> None:
        cache_service.store_tweet(tweet)
        storage_service.store_tweet(tweet)

    def get_all_tweets(self) -> List[Tweet]:
        if not cache_service.load_tweets():
            tweets = storage_service.load_tweets()
            cache_service.store_tweets(tweets)

        return cache_service.load_tweets()


tweet_service = TweetService()
