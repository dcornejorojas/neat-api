from flask import request
from src.rest.middlewares import middleware_accepted_adoption
from src.rest.controllers import Controllers

def create_routes(app) -> None:
    controllers = Controllers()

    @app.route("/", methods=["GET"])
    def default():
        return controllers.default_route()
    
    @app.route("/health", methods=["GET"])
    def health():
        return controllers.health_route()

    @app.route("/pokemon/list", methods=["GET"])
    def pokemon_list():
        return controllers.pokemon_list()

    @app.route("/pokemon/healthcare", methods=["POST"])
    def pokemon_healthcare():
        return controllers.pokemon_healthcare(request)

    @app.route("/trainer/adoption", methods=["POST"])
    @middleware_accepted_adoption()
    def load_promotions():
        return controllers.trainer_adoption(request)

    @app.route("/trainer/status", methods=["GET"])
    def get_promotions():
        return controllers.trainer_status(request)
