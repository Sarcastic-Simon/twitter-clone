from os.path import join

from models.tweet import Tweet
from models.user import User


class FilenameService:
    def __init__(self, storage_location: str = 'storage',
                 user_folder='users',
                 tweet_folder='tweets',
                 filename_pattern: str = '%Y-%m-%d-%H-%M-%S-%f') -> None:
        self.storage_location = storage_location
        self.user_folder = user_folder
        self.tweet_folder = tweet_folder
        self.filename_pattern = filename_pattern

    def tweet_load_path(self, filename: str) -> str:
        return join(self.tweets(), filename)

    def tweet_store_path(self, tweet: Tweet) -> str:
        name = tweet.date_published.strftime(self.filename_pattern)
        path = join(self.tweets(), name)
        return path + '.json'

    def get_input_file_path(self, filename: str) -> str:
        return join(self.storage_location, filename)

    def get_output_file_path(self, tweet: Tweet) -> str:
        filename = tweet.date_published.strftime(self.filename_pattern)
        file_path = join(self.storage_location, filename)
        return file_path + '.json'

    def user_save_path(self, user: User) -> str:
        filename = user.username
        file_path = join(self.storage_location, self.user_folder, filename)
        return file_path + '.json'

    def user_load_path(self, username: str) -> str:
        path = join(self.storage_location, self.user_folder, username)
        return path + '.json'

    def tweets(self):
        return join(self.storage_location, self.tweet_folder)
