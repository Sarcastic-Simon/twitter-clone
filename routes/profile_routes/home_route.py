from flask import request, url_for, render_template, g
from werkzeug.utils import redirect

from services.tweet_service import get_follower_tweets, post_tweet


def home_route():
    if request.method == 'POST':
        post_tweet(g.user.username,
                   request.form['message'])
        return redirect(url_for('profile', username=g.user.username))
    else:
        return render_template('index.html',
                               tweets=get_follower_tweets(g.user))
