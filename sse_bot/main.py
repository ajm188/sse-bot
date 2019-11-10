from flask import Flask

from sse_bot import views


def create_app():
    app = Flask(__name__)
    app.register_blueprint(views.routes)
    return app


def main():
    create_app().run()


if __name__ == "__main__":
    main()
