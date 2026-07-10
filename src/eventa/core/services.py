from datetime import UTC, datetime
from typing import Any

from eventa.storage.base import Storage


class EventService:
    """Validates and records events. Owns no infrastructure details —
    delegates persistence to the injected Storage."""

    def __init__(self, storage: Storage) -> None:
        self._storage = storage

    def track(self, event: str, user: str | None, properties: dict[str, Any] | None) -> None:
        if not event or not event.strip():
            raise ValueError("event must be a non-empty string")

        self._storage.save_event(
            event_name=event,
            user=user,
            properties=properties or {},
            created_at=datetime.now(UTC),
        )
