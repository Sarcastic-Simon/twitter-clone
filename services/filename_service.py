from os.path import join

from config.constants import tweets_folder, filename_pattern, users_folder
from models.tweet import Tweet
from models.user import User


class FilenameService:
    def tweet_load_path(self, filename: str) -> str:
        return join(tweets_folder, filename)

    def tweet_store_path(self, tweet: Tweet) -> str:
        name = self._tweet_filename(tweet)
        path = join(tweets_folder, name)
        return path + '.json'

    def _tweet_filename(self, tweet: Tweet) -> str:
        return tweet.date_published.strftime(filename_pattern)

    def user_load_path(self, username: str) -> str:
        path = join(users_folder, username)
        return path + '.json'

    def user_store_path(self, user: User) -> str:
        return join(users_folder, user.username) + '.json'


filename_service = FilenameService()
