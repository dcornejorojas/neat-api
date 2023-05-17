from src.infrastructure.repository import Repository
from typing import Tuple
import http

class AdoptionStatus:
    def __init__(self, data):
        self.repository = Repository()
        self.data = data

    def execute(self) -> Tuple[str,int]:
        try:
            response = self.repository.view_adoption_status(self.data) or {}
            return {"status": "accepted", "message": "Estado de solicitud de adopción", "response": response}, http.HTTPStatus.BAD_REQUEST
        except Exception as e:
            return str(e), http.HTTPStatus.INTERNAL_SERVER_ERROR