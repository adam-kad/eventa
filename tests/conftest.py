import pytest

from eventa import Analytics


@pytest.fixture
def analytics() -> Analytics:
    return Analytics(database="sqlite:///:memory:")
