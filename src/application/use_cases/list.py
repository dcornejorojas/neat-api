from src.infrastructure.repository import Repository
from typing import Tuple
import http

class List:
    def __init__(self):
        self.repository = Repository()

    def execute(self) -> Tuple[str,int]:
        try:
            response = self.repository.get_pokemon_list(self.data) or []
            return {"status": "accepted", "message": "Lista de pokemons sin adoptar", "response": response}, http.HTTPStatus.BAD_REQUEST
        except Exception as e:
            return str(e), http.HTTPStatus.INTERNAL_SERVER_ERROR