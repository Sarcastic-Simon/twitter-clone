from os import listdir
from typing import List

from jsonpickle import encode, decode

from models.tweet import Tweet
from services.filename_service import FilenameService


class StorageService:
    def __init__(self, filename_service=FilenameService()) -> None:
        self.filename_service = filename_service

    def store_tweet(self, tweet: Tweet) -> None:
        file_path = self.filename_service.get_output_file_path(tweet)
        with open(file_path, 'w') as file:
            encoded = encode(tweet)
            file.write(encoded)

    def load_tweets(self) -> List[Tweet]:
        result = []
        for filename in listdir(self.filename_service.storage_location):
            file_path = self.filename_service.get_input_file_path(filename)
            with open(file_path, 'r') as file:
                tweet = decode(file.read())
                result.append(tweet)
        return result
