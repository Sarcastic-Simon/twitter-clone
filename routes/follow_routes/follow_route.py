from flask import url_for, g
from werkzeug.utils import redirect

from services.follow_service import add_follower


def follow_route(username: str):
    add_follower(g.user, username)
    return redirect(url_for('home'))
