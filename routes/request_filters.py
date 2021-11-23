from functools import wraps

from flask import g, url_for
from werkzeug.utils import redirect


def login_required(function):
    @wraps(function)
    def challenge_credentials(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        return function(*args, **kwargs)

    return challenge_credentials
