from os import listdir
from os.path import join

from jsonpickle import encode, decode

from models.tweet import Tweet


class TweetService:

    def __init__(
            self,
            storage_location='storage',
            filename_pattern='%Y-%m-%d-%H-%M-%S-%f'):
        self.cache = []
        self.storage_location = storage_location
        self.filename_pattern = filename_pattern

    def save_tweet(self, tweet: Tweet):
        with open(self._get_output_file_path(tweet), 'w') as file:
            encoded = encode(tweet)
            file.write(encoded)
        self.cache.append(tweet)

    def get_all_tweets(self):
        if not self.cache:
            for filename in listdir(self.storage_location):
                with open(self._get_input_file_name(filename), 'r') as file:
                    tweet = decode(file.read())
                    self.cache.append(tweet)

        return self.cache

    def _get_input_file_name(self, filename):
        return join(
            self.storage_location,
            filename)

    def _get_output_file_path(self, tweet: Tweet) -> str:
        file_path = join(
            self.storage_location,
            tweet.date_published.strftime(self.filename_pattern))
        return file_path + '.json'
