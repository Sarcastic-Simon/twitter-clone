from os import getenv

from flask_humanize import Humanize

from config import setup_user


def configure_flask(app):
    app.secret_key = getenv('TWITTER_SECRET_KEY')
    Humanize(app)

    @app.before_request
    def setup_context(): setup_user()

