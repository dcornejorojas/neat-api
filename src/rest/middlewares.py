import http
from flask import request
from random import random
from functools import wraps

def middleware_accepted_adoption() -> any:
    def _home_decorator(f):
        @wraps(f)
        def __home_decorator(*args, **kwargs):
            if random() > .50:
                return f(*args, **kwargs)
            return {"status": "denied", "message": "Primer filtro en el proceso de adopcion rechazado por parametros internos", "acceptance_criteria": "<50%"}, http.HTTPStatus.BAD_REQUEST
        return __home_decorator
    return _home_decorator
