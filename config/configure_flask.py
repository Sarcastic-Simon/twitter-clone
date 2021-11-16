from os import getenv

from flask_humanize import Humanize


def configure_flask(app):
    app.secret_key = getenv('TWITTER_SECRET_KEY')
    Humanize(app)
