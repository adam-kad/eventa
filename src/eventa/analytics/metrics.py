from eventa.storage.base import Storage


class Metrics:
    """Basic aggregation over stored events. Only what MVP requires
    (event count) is implemented; DAU/WAU/retention/funnels/cohorts
    are future work."""

    def __init__(self, storage: Storage) -> None:
        self._storage = storage

    def count_events(self, event: str | None = None) -> int:
        return self._storage.count_events(event_name=event)
