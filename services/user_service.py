from typing import Optional

from models import User
from services.cache_service import load_user_from_cache, store_user_in_cache
from services.storage_service import load_user_from_disk, store_user_on_disk


def get_user(username: str = None) -> Optional[User]:
    if username is None:
        return None
    return (load_user_from_cache(username)
            or load_user_from_disk(username))


def create_user(username: str, password: str) -> User:
    user = User(username, password)
    store_user_in_cache(user)
    store_user_on_disk(user)
    return user
