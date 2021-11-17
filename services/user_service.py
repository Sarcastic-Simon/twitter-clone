from typing import Optional

from models import User
from services.cache_service import load_user_from_cache
from services.storage_service import load_user_from_disk


def get_user(username: str = None) -> Optional[User]:
    if username is None:
        return None
    return (load_user_from_cache(username)
            or load_user_from_disk(username))
