from flask import url_for, g
from werkzeug.utils import redirect

from services.user_service import add_follower


def follow_route(username: str):
    if g.user is None:
        return redirect(url_for('login_page'))
    add_follower(g.user, username)
    return redirect(url_for('home_page'))
