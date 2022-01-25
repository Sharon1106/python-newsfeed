# imports home bp
from app.routes import home, dashboard

# needed to run flask
from flask import Flask
from app.db import init_db


def create_app(test_config=None):
    # set up app config
    app = Flask(__name__, static_url_path="/")
    app.url_map.strict_slashes = False
    app.config.from_mapping(SECRET_KEY="super_secret_key")

    @app.route("/hello")
    def hello():
        init_db(app)
        return "Hello world!"

    # register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    return app
