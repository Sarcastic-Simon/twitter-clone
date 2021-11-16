from flask import render_template, g, url_for
from werkzeug.utils import redirect

from services.tweet_service import get_other_tweets


def explore_route():
    if g.user is None:
        return redirect(url_for('login'))

    return render_template('explore.html',
                           tweets=get_other_tweets(g.user))
