from typing import Optional

from werkzeug.security import check_password_hash

from models import User
from services.user_service import get_user, create_user


def register(username: str, password: str) -> Optional[User]:
    user = get_user(username)
    if user is not None:
        return None
    return create_user(username, password)


def login(username: str, password: str) -> Optional[User]:
    user = get_user(username)
    if user and check_password_hash(user.password, password):
        return user
