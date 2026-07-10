from datetime import datetime
from typing import Any

from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import Session

from eventa.models.event import Base, Event
from eventa.storage.base import Storage


class SQLAlchemyStorage(Storage):
    """SQLAlchemy-backed storage. Works with any SQLAlchemy connection URL
    (SQLite today, other SQL databases later) without changing the API."""

    def __init__(self, database: str) -> None:
        self._engine = create_engine(database)

    def create_schema(self) -> None:
        # Base is private to eventa (its metadata holds only Event), so this
        # creates exactly eventa's own table and touches nothing else.
        Base.metadata.create_all(self._engine)

    def save_event(
        self,
        event_name: str,
        user: str | None,
        properties: dict[str, Any],
        created_at: datetime,
    ) -> None:
        with Session(self._engine) as session:
            session.add(
                Event(
                    event_name=event_name,
                    user=user,
                    properties=properties,
                    created_at=created_at,
                )
            )
            session.commit()

    def count_events(self, event_name: str | None = None) -> int:
        stmt = select(func.count()).select_from(Event)
        if event_name is not None:
            stmt = stmt.where(Event.event_name == event_name)

        with Session(self._engine) as session:
            return session.scalar(stmt) or 0
