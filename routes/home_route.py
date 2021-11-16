from typing import List, Dict

from flask import request, url_for, render_template, g
from werkzeug.utils import redirect

from models.tweet import Tweet
from services.tweet_service import (save_tweet, get_all_tweets,
                                    get_follower_tweets, get_my_tweets)


def home_route():
    if request.method == 'POST':
        if g.user is None:
            return redirect(url_for('login'))
        save_tweet(Tweet(g.user.username, request.form['message']))

    return render_template('index.html', **_build_context())


def _build_context() -> Dict[str, List[Tweet]]:
    return {
        'follower_tweets': get_follower_tweets(g.user),
        'my_tweets': get_my_tweets(g.user),
        'all_tweets': get_all_tweets(g.user)
    }
