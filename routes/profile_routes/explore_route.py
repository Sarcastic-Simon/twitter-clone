from flask import render_template, g

from services.tweet_service import get_other_tweets


def explore_route():
    return render_template('explore.html',
                           tweets=get_other_tweets(g.user))
