import pytest

from eventa import Analytics


def test_track_creates_event(analytics: Analytics) -> None:
    analytics.track(event="login", user="user_123", properties={"source": "web"})

    assert analytics.count_events() == 1
    assert analytics.count_events(event="login") == 1
    assert analytics.count_events(event="logout") == 0


def test_track_without_user_and_properties(analytics: Analytics) -> None:
    analytics.track(event="app_start")

    assert analytics.count_events() == 1


def test_track_rejects_empty_event(analytics: Analytics) -> None:
    with pytest.raises(ValueError):
        analytics.track(event="")
