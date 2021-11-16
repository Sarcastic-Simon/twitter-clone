from routes.auth_routes.login_route import login_route
from routes.auth_routes.logout_route import logout_route
from routes.auth_routes.register_route import register_route


def register_auth_routes(app):
    @app.route("/register", methods=['GET', 'POST'])
    def register(): return register_route()

    @app.route("/login", methods=['GET', 'POST'])
    def login(): return login_route()

    @app.route("/logout")
    def logout(): return logout_route()
