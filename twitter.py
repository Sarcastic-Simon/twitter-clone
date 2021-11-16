from flask import Flask

from config.configure_flask import configure_flask
from routes.auth_routes import register_auth_routes
from routes.follow_routes import register_follow_routes
from routes.profile_routes import register_profile_routes

app = Flask(__name__)
configure_flask(app)
register_profile_routes(app)
register_follow_routes(app)
register_auth_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
