from typing import Optional

from bcrypt import checkpw

from models.user import User
from services.cache_service import store_user_in_cache, load_user_from_cache
from services.storage_service import store_user_on_disk, load_user_from_disk


def register(username: str, password: str) -> Optional[User]:
    if not username or not password:
        return None
    user = User(username, password)
    store_user_in_cache(user)
    store_user_on_disk(user)
    return user


def login(username: str, password: str) -> Optional[User]:
    user = load_user_from_cache(username)
    if user is None:
        user = load_user_from_disk(username)
    if user is not None:
        if checkpw(password.encode(), user.password):
            return user
