import pytest

from repositories.prediction import PredictionRepository


def test_get_returns_none_for_unknown_item():
    repository = PredictionRepository()

    assert repository.get(item_id=10) is None


@pytest.mark.parametrize("is_allowed", [True, False])
def test_save_makes_decision_available(is_allowed):
    repository = PredictionRepository()

    repository.save(item_id=10, is_allowed=is_allowed)

    assert repository.get(item_id=10) is is_allowed


def test_save_replaces_previous_decision():
    repository = PredictionRepository()
    repository.save(item_id=10, is_allowed=True)

    repository.save(item_id=10, is_allowed=False)

    assert repository.get(item_id=10) is False