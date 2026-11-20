from repositories.prediction import PredictionRepository


def predict(
    item_id: int,
    is_verified_seller: bool,
    images_qty: int,
    repository: PredictionRepository,
) -> bool:
    is_allowed = is_verified_seller or images_qty > 0
    repository.save(item_id=item_id, is_allowed=is_allowed)
    return is_allowed