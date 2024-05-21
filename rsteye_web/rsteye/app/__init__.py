from flask import Flask

from .views import main


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "FesC9cBSuxakv9yN0vBY"

    app.register_blueprint(main)
    return app
