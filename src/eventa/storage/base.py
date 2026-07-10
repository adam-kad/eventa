from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


class Storage(ABC):
    """Persistence contract for events. Implementations must not touch
    any tables other than their own."""

    @abstractmethod
    def create_schema(self) -> None: ...

    @abstractmethod
    def save_event(
        self,
        event_name: str,
        user: str | None,
        properties: dict[str, Any],
        created_at: datetime,
    ) -> None: ...

    @abstractmethod
    def count_events(self, event_name: str | None = None) -> int: ...
