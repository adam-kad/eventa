from typing import Any

from eventa.analytics.metrics import Metrics
from eventa.core.services import EventService
from eventa.storage.sqlite import SQLAlchemyStorage


class Analytics:
    """The single public entry point of Eventa."""

    def __init__(self, database: str = "sqlite:///eventa.db") -> None:
        storage = SQLAlchemyStorage(database)
        storage.create_schema()

        self._service = EventService(storage)
        self._metrics = Metrics(storage)

    def track(
        self,
        event: str,
        user: str | None = None,
        properties: dict[str, Any] | None = None,
    ) -> None:
        self._service.track(event=event, user=user, properties=properties)

    def count_events(self, event: str | None = None) -> int:
        return self._metrics.count_events(event)
