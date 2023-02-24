from flask import Flask


def create_app():
    """Create and configure the Flask app"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "11yagsimiznat11"

    # Include the routes from app.py
    with app.app_context():
        from . import hello

    return app
#python -m flask --app 'house_price_app:create_app()' --debug run