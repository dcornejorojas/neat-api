from src.infrastructure.repository import Repository
from random import random
from typing import Tuple
import http

class Adoption:
    def __init__(self, data):
        self.repository = Repository()
        self.data = data

    def execute(self) -> Tuple[str,int]:
        try:
            is_valid = self.repository.valid_trainer(self.data) or False
            if is_valid and random() > .05:
                response = self.repository.valid_adoption(self.data) or {}
                return {"status": "accepted", "message": "Proceso de adopcion realizado exitosamente. Felicidades", "response": response}, http.HTTPStatus.OK
            else:
                return {"message": "Segundo filtro en el proceso de adopcion rechazado por parametros internos", "acceptance_criteria": "<95%"}, http.HTTPStatus.BAD_REQUEST
        except Exception as e:
            return str(e), http.HTTPStatus.INTERNAL_SERVER_ERROR
        
