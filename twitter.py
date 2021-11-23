from flask import Flask

from config import configure_flask
from routes import (register_auth_routes,
                    register_follow_routes,
                    register_profile_routes)

app = Flask(__name__)
configure_flask(app)
register_profile_routes(app)
register_follow_routes(app)
register_auth_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
