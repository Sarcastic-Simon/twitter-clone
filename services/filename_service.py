from os.path import join

from models.tweet import Tweet


class FilenameService:
    def __init__(self, storage_location: str = 'storage',
                 filename_pattern: str = '%Y-%m-%d-%H-%M-%S-%f') -> None:
        self.storage_location = storage_location
        self.filename_pattern = filename_pattern

    def get_input_file_path(self, filename: str) -> str:
        return join(self.storage_location, filename)

    def get_output_file_path(self, tweet: Tweet) -> str:
        filename = tweet.date_published.strftime(self.filename_pattern)
        file_path = join(self.storage_location, filename)
        return file_path + '.json'
