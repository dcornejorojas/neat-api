import http
from flask import make_response, jsonify, render_template
from src.domain.trainer.api_rest import TrainerApiRest
from src.domain.pokemon.api_rest import PokemonApiRest


class Controllers:
    def __init__(self) -> any:
        self.error_message_contact_admin = (
            "Error desconocido, favor contactese con el administrador"
        )
        self.trainer_api_rest = TrainerApiRest()
        self.pokemon_api_rest = PokemonApiRest()

    def default_route(self) -> any:
        template = render_template('index.html')
        return make_response(template)
    
    def health_route(self) -> any:
        return make_response({"status": "success", "message": "API health check"}, http.HTTPStatus.OK)

    def pokemon_healthcare(self, request) -> any:
        try:
            if not request.is_json:
                return make_response(
                    jsonify({"status": "error", "message": "Debe ingresar información en formato JSON"}), http.HTTPStatus.BAD_REQUEST
                )
            response = self.pokemon_api_rest.process_healthcare(request) or {}
            return make_response(jsonify({"message": response}), http.HTTPStatus.OK)
        except Exception as e:
            return make_response(
                jsonify({"status": "error","message": self.error_message_contact_admin}), http.HTTPStatus.INTERNAL_SERVER_ERROR
            )
    
    def pokemon_list(self) -> any:
        try:
            response = self.pokemon_api_rest.get_list() or []
            return make_response(jsonify({"status": "success", "message": response}), http.HTTPStatus.OK)
        except Exception as e:
            return make_response(
                jsonify({"status": "error","message": self.error_message_contact_admin}), http.HTTPStatus.INTERNAL_SERVER_ERROR
            )

    def trainer_adoption(self, request) -> any:
        try:
            if not request.is_json:
                return make_response(
                    jsonify({"status": "error","message": "Debe enviar la información necesaria en formato JSON"}), http.HTTPStatus.BAD_REQUEST
                )
            response, code = self.trainer_api_rest.process_adoption(request) or {}
            if code != http.HTTPStatus.OK:
                return make_response(jsonify({"status": "error","message": response}), code)
            return make_response(jsonify({"status": "success","message": response}), http.HTTPStatus.OK)
        except Exception as e:
            return make_response(jsonify({"status": "error","message": str(e)}), http.HTTPStatus.INTERNAL_SERVER_ERROR)

    def trainer_status(self, request) -> any:
        try:
            if not request.is_json:
                return make_response(
                    jsonify({"status": "error","message": "Debe enviar la información necesaria en formato JSON"}), http.HTTPStatus.BAD_REQUEST
                )
            response = self.trainer_api_rest.view_adoption_status(request) or {}
            return make_response(jsonify({"status": "success","message": response}), http.HTTPStatus.OK)
        except Exception as e:
            return make_response(
                jsonify(
                    {
                        "status": "error",
                        "message": self.error_message_contact_admin,
                        "exception": str(e),
                    }
                ),
                http.HTTPStatus.INTERNAL_SERVER_ERROR,
            )