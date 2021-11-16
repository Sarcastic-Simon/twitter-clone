from typing import Optional

from werkzeug.security import check_password_hash

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
    user = get_user(username)
    if user is not None:
        if check_password_hash(user.password, password):
            return user


def add_follower(user: User, username: str) -> None:
    user.followers.add(username)
    store_user_in_cache(user)
    store_user_on_disk(user)


def remove_follower(user: User, username: str) -> None:
    user.followers.remove(username)
    store_user_in_cache(user)
    store_user_on_disk(user)


def get_user(username: str = None) -> Optional[User]:
    if username is None:
        return None
    return (load_user_from_cache(username)
            or load_user_from_disk(username))
