from typing import Optional

from bcrypt import checkpw

from models.user import User
from services.cache_service import cache_service
from services.storage_service import storage_service


class UserService:
    def register(self, username: str, password: str) -> Optional[User]:
        if not username or not password:
            return None
        user = User(username, password)
        cache_service.store_user(user)
        storage_service.store_user(user)
        return user

    def login(self, username: str, password: str) -> Optional[User]:
        user = cache_service.load_user(username)
        if user is None:
            user = storage_service.load_user(username)
        if user is not None:
            if checkpw(password.encode(), user.password):
                return user


user_service = UserService()
