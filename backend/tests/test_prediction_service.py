import pytest

from services.prediction import predict


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
    is_verified_seller: bool,
    images_qty: int,
    expected: bool,
    repository,
):
    result = predict(
        item_id=10,
        is_verified_seller=is_verified_seller,
        images_qty=images_qty,
        repository=repository,
    )

    assert result is expected
    assert repository.get(item_id=10) is expected