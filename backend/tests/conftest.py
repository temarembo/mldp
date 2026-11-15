import pytest
from fastapi.testclient import TestClient
from dependencies import get_prediction_repository
from repositories.prediction import PredictionRepository

from main import app


@pytest.fixture
def repository():
    return PredictionRepository()


@pytest.fixture
def client(repository):
    app.dependency_overrides[get_prediction_repository] = lambda: repository

    try:
        with TestClient(app, raise_server_exceptions=False) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(get_prediction_repository, None)


@pytest.fixture
def valid_payload():
    return {
        "seller_id": 1,
        "is_verified_seller": False,
        "item_id": 10,
        "name": "Велосипед",
        "description": "Почти новый",
        "category": 2,
        "images_qty": 1,
    }