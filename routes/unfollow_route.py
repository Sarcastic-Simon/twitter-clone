from flask import url_for, g
from werkzeug.utils import redirect

from services.user_service import remove_follower


def unfollow_route(username: str):
    if g.user is None:
        return redirect(url_for('login_page'))
    remove_follower(g.user, username)
    return redirect(url_for('home_page'))
