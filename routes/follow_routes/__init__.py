from routes.follow_routes.follow_route import follow_route
from routes.follow_routes.unfollow_route import unfollow_route


def register_follow_routes(app):
    @app.route("/follow/<username>/")
    def follow(username: str): return follow_route(username)

    @app.route("/unfollow/<username>")
    def unfollow(username: str): return unfollow_route(username)
