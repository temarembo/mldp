class PredictionRepository:
    def __init__(self) -> None:
        self._results: dict[int, bool] = {}

    def save(self, item_id: int, is_allowed: bool) -> None:
        self._results[item_id] = is_allowed

    def get(self, item_id: int) -> bool | None:
        return self._results.get(item_id)