from src.infrastructure.repository import Repository
from typing import Tuple
import http

class HealthCare:
    def __init__(self, data):
        self.repository = Repository()
        self.data = data

    def execute(self) -> Tuple[str,int]:
        try:
            response = self.repository.get_healthcare(self.data) or {}
            return {"status": "accepted", "message": "Proceso de envio para cuidados médicos realizado exitosamente. Pronta recuperación", "response": response}, http.HTTPStatus.BAD_REQUEST
        except Exception as e:
            return str(e), http.HTTPStatus.INTERNAL_SERVER_ERROR