from repositories.prediction import PredictionRepository

_repository = PredictionRepository()


def get_prediction_repository() -> PredictionRepository:
    return _repository