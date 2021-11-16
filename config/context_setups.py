from flask import session, g

from services.user_service import get_user


def setup_user():
    g.user = get_user(session.get('username'))
