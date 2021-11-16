from flask import Flask

from config.configure_flask import configure_flask
from config.context_setups import setup_user
from routes.follow_route import follow_route
from routes.home_route import home_route
from routes.login_route import login_route
from routes.logout_route import logout_route
from routes.register_route import register_route
from routes.unfollow_route import unfollow_route

app = Flask(__name__)
configure_flask(app)


@app.before_request
def setup_context(): setup_user()


@app.route("/", methods=['GET', 'POST'])
def home_page(): return home_route()


@app.route("/follow/<username>")
def follow_page(username: str): return follow_route(username)


@app.route("/unfollow/<username>")
def unfollow_page(username: str): return unfollow_route(username)


@app.route("/register", methods=['GET', 'POST'])
def register_page(): return register_route()


@app.route("/login", methods=['GET', 'POST'])
def login_page(): return login_route()


@app.route("/logout")
def logout_page(): return logout_route()


if __name__ == '__main__':
    app.run(debug=True)
