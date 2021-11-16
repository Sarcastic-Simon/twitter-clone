from flask import session, url_for
from werkzeug.utils import redirect


def logout_route():
    session.pop('username')
    return redirect(url_for('home'))
