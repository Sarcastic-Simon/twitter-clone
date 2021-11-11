from flask import Flask, render_template, request
from flask_humanize import Humanize

from models.tweet import Tweet
from services.tweet_service import TweetService

app = Flask(__name__)
Humanize(app)

tweet_service = TweetService()


@app.route("/", methods=['GET', 'POST'])
def home_page() -> str:
    if request.method == 'POST':
        author = request.form['author']
        message = request.form['message']
        tweet = Tweet(author, message)
        tweet_service.save_tweet(tweet)

    return render_template(
        'index.html',
        tweets=tweet_service.get_all_tweets())


if __name__ == '__main__':
    app.run(debug=True)
