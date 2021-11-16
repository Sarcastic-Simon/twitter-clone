from flask import request, url_for, render_template, g
from werkzeug.utils import redirect

from models.tweet import Tweet
from services.tweet_service import (save_tweet, get_follower_tweets)


def home_route():
    if g.user is None:
        return redirect(url_for('login'))

    if request.method == 'POST':
        save_tweet(Tweet(g.user.username, request.form['message']))

    return render_template('index.html',
                           tweets=get_follower_tweets(g.user))
