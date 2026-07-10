from datetime import datetime
from typing import Any

from sqlalchemy import JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = "eventa_events"

    id: Mapped[int] = mapped_column(primary_key=True)
    event_name: Mapped[str]
    user: Mapped[str | None]
    created_at: Mapped[datetime]
    properties: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
