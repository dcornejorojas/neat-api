import os
from flask import Flask
from flask_cors import CORS

from src.rest import create_routes


class Server():
    def __init__(self) -> None:
        self.cors = CORS()
        pass

    def create_server(self) -> Flask:
        app = Flask(__name__)
        with app.app_context():
            self.cors.init_app(app, resources={r"*": {"origins": "*"}})
            create_routes(app)

        return app

app = Server().create_server()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", port=int(os.getenv("PORT_FLASK",8080)), debug=False, threaded=True
    )
