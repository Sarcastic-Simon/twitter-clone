from flask import request, session, url_for, render_template
from werkzeug.utils import redirect

from models.tweet import Tweet
from services.tweet_service import tweet_service


def home_page_route():
    if request.method == 'POST':
        if 'username' not in session:
            return redirect(url_for('login'))
        author = session['username']
        message = request.form['message']
        tweet = Tweet(author, message)
        tweet_service.save_tweet(tweet)

    return render_template('index.html',
                           tweets=tweet_service.get_all_tweets())
