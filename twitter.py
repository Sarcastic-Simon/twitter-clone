from flask import Flask, render_template, request

from models.tweet import Tweet

app = Flask(__name__)

tweets = []


@app.route("/", methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        author = request.form['author']
        message = request.form['message']
        tweet = Tweet(author, message)
        tweets.append(tweet)

    return render_template('index.html', tweets=tweets)
