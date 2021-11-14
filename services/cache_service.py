from typing import List

from models.tweet import Tweet
from models.user import User


class CacheService:
    def __init__(self) -> None:
        self.tweets = []
        self.users = {}

    def store_tweet(self, tweet: Tweet) -> None:
        self.tweets.append(tweet)

    def store_tweets(self, tweets: List[Tweet]) -> None:
        for tweet in tweets:
            self.tweets.append(tweet)

    def load_tweets(self) -> List[Tweet]:
        return self.tweets

    def store_user(self, user: User) -> None:
        self.users[user.username] = user

    def load_user(self, username: str) -> User:
        return self.users.get(username)


cache_service = CacheService()
