from routes.profile_routes.explore_route import explore_route
from routes.profile_routes.home_route import home_route
from routes.profile_routes.profile_route import profile_route


def register_profile_routes(app):
    @app.route("/", methods=['GET', 'POST'])
    def home(): return home_route()

    @app.route("/profile/<username>")
    def profile(username: str): return profile_route(username)

    @app.route("/explore/")
    def explore(): return explore_route()
