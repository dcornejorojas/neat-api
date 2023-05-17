from src.application.use_cases.healthcare import HealthCare
from src.application.use_cases.list import List


class PokemonApiRest:
    def __init__(self):
        pass

    def process_healthcare(self,data) -> None:
        use_case = HealthCare(data)
        response = use_case.execute()
        return response
    
    def get_list(self) -> None:
        use_case = List()
        response = use_case.execute()
        return response