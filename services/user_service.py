from bcrypt import checkpw

from models.user import User
from services.cache_service import CacheService
from services.storage_service import StorageService


class UserService:
    def __init__(self, cache_service=CacheService(),
                 storage_service=StorageService()):
        self.cache = cache_service
        self.storage_service = storage_service

    def register(self, username: str, password: str):
        if not username or not password:
            return None
        user = User(username, password)
        self.cache.store_user(user)
        self.storage_service.store_user(user)
        return user

    def login(self, username: str, password: str):
        user = self.cache.load_user(username)
        if user is None:
            user = self.storage_service.load_user(username)
        if user is not None:
            if checkpw(password.encode(), user.password):
                return user


user_service = UserService()
