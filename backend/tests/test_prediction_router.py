import pytest


@pytest.mark.parametrize(
    ("is_verified_seller", "images_qty", "expected"),
    [
        (True, 0, True),
        (True, 1, True),
        (False, 0, False),
        (False, 1, True),
    ],
)
def test_predict_returns_expected_decision(
    client, valid_payload, is_verified_seller, images_qty, expected, repository
):
    valid_payload["is_verified_seller"] = is_verified_seller
    valid_payload["images_qty"] = images_qty

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 200
    assert response.json() is expected
    assert repository.get(item_id=valid_payload["item_id"]) is expected


@pytest.mark.parametrize(
    "field",
    [
        "seller_id",
        "is_verified_seller",
        "item_id",
        "name",
        "description",
        "category",
        "images_qty",
    ],
)
def test_predict_returns_400_when_required_field_is_missing(
    client, valid_payload, field
):
    del valid_payload[field]

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 400
    assert any(
        error["loc"] == ["body", field]
        for error in response.json()["detail"]
    )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("seller_id", "abc"),
        ("is_verified_seller", "true"),
        ("item_id", "abc"),
        ("name", 123),
        ("description", 123),
        ("category", "abc"),
        ("images_qty", "1"),
    ],
)
def test_predict_returns_400_when_field_has_wrong_type(
    client, valid_payload, field, value
):
    valid_payload[field] = value

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 400
    assert any(
        error["loc"] == ["body", field]
        for error in response.json()["detail"]
    )


def test_predict_returns_400_when_json_is_malformed(client):
    response = client.post(
        "/predict",
        content="{",
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400


def test_predict_returns_500_when_service_fails(
    client, valid_payload, monkeypatch
):
    def broken_predict(*args, **kwargs):
        raise RuntimeError("Simulated service failure")

    monkeypatch.setattr("routers.prediction.predict", broken_predict)

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 500
    assert response.json() == {"detail": "Internal server error"}