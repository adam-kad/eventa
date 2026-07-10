from datetime import UTC, datetime

from eventa.storage.sqlite import SQLAlchemyStorage


def test_save_and_count_events() -> None:
    storage = SQLAlchemyStorage("sqlite:///:memory:")
    storage.create_schema()

    storage.save_event(
        event_name="purchase",
        user="telegram:123",
        properties={"amount": 299},
        created_at=datetime.now(UTC),
    )

    assert storage.count_events() == 1
    assert storage.count_events(event_name="purchase") == 1
    assert storage.count_events(event_name="refund") == 0
