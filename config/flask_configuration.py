from os import getenv

from flask import session, g
from flask_humanize import Humanize

from services.user_service import get_user


def configure_flask(app):
    app.secret_key = getenv('TWITTER_SECRET_KEY')
    Humanize(app)

    @app.before_request
    def setup_context():
        g.user = get_user(session.get('username'))
