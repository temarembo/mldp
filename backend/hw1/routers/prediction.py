from fastapi import APIRouter, Depends

from dependencies import get_prediction_repository
from models.prediction import PredictionRequest
from repositories.prediction import PredictionRepository
from services.prediction import predict

router = APIRouter()


@router.post("/predict", response_model=bool)
async def predict_endpoint(
    ad: PredictionRequest,
    repository: PredictionRepository = Depends(get_prediction_repository),
) -> bool:
    return predict(
        item_id=ad.item_id,
        is_verified_seller=ad.is_verified_seller,
        images_qty=ad.images_qty,
        repository=repository,
    )