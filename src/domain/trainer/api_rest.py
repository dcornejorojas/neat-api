from src.application.use_cases.adoption import Adoption


class TrainerApiRest:
    def __init__(self):
        pass

    def process_adoption(self,data) -> None:
        use_case = Adoption(data)
        response = use_case.execute()
        return response