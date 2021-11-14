from flask import request, session, url_for, render_template
from werkzeug.utils import redirect

from models.tweet import Tweet
from services.tweet_service import save_tweet, get_all_tweets


def home_page_route():
    if request.method == 'POST':
        if 'username' not in session:
            return redirect(url_for('login'))
        author = session['username']
        message = request.form['message']
        tweet = Tweet(author, message)
        save_tweet(tweet)

    return render_template('index.html',
                           tweets=get_all_tweets())
