from os import getenv

from flask import Flask
from flask_humanize import Humanize

from routes.home_page_route import home_page_route
from routes.login_route import login_route
from routes.logout_route import logout_route
from routes.register_route import register_route

app = Flask(__name__)
app.secret_key = getenv('TWITTER_SECRET_KEY')
Humanize(app)


@app.route("/", methods=['GET', 'POST'])
def home_page(): return home_page_route()


@app.route("/register", methods=['GET', 'POST'])
def register_page(): return register_route()


@app.route("/login", methods=['GET', 'POST'])
def login_page(): return login_route()


@app.route("/logout")
def logout_page(): return logout_route()


if __name__ == '__main__':
    app.run(debug=True)
