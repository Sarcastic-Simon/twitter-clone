from flask import render_template, g, url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from services.tweet_service import get_user_tweets
from services.user_service import get_user


def profile_route(username: str):
    if g.user is None:
        return redirect(url_for('login'))

    user = get_user(username) or abort(404)
    return render_template('profile.html',
                           username=username,
                           tweets=get_user_tweets(user))
