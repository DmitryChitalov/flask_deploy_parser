from flask import Flask


def create_app():
    app = Flask(__name__)

    from flask_parser.flask_parser.flask_parser import parser_blueprint

    app.register_blueprint(parser_blueprint)

    return app
