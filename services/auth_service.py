from typing import Optional

from werkzeug.security import check_password_hash

from models import User
from services.user_service import get_user
from services.cache_service import store_user_in_cache
from services.storage_service import store_user_on_disk


def register(username: str, password: str) -> Optional[User]:
    user = get_user(username)
    if user is not None:
        return None
    user = User(username, password)
    store_user_in_cache(user)
    store_user_on_disk(user)
    return user


def login(username: str, password: str) -> Optional[User]:
    user = get_user(username)
    if user and check_password_hash(user.password, password):
        return user
