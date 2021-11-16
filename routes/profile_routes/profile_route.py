from flask import render_template
from werkzeug.exceptions import abort

from services.tweet_service import get_user_tweets
from services.user_service import get_user


def profile_route(username: str):
    user = get_user(username) or abort(404)
    return render_template('profile.html',
                           username=username,
                           tweets=get_user_tweets(user))
