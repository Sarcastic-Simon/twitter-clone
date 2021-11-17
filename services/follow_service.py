from models import User
from services.cache_service import store_user_in_cache
from services.storage_service import store_user_on_disk


def add_follower(user: User, username: str) -> None:
    user.followers.add(username)
    store_user_in_cache(user)
    store_user_on_disk(user)


def remove_follower(user: User, username: str) -> None:
    user.followers.remove(username)
    store_user_in_cache(user)
    store_user_on_disk(user)
