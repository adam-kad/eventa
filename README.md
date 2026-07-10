# Eventa

Lightweight, local-first event analytics for Python applications — no external services required.

```python
from eventa import Analytics

analytics = Analytics(database="sqlite:///eventa.db")

analytics.track(
    event="payment_success",
    user="telegram:123456",
    properties={"plan": "premium", "price": 299},
)
```

## Install

```bash
pip install eventa
```

## Usage

```python
from eventa import Analytics

analytics = Analytics()  # defaults to sqlite:///eventa.db

analytics.track(event="login", user="user_123")
analytics.track(event="button_click", user="user_123", properties={"button": "buy"})

analytics.count_events()                 # total events
analytics.count_events(event="login")    # events of a given name
```

`user` is just a string identifier you control — Eventa doesn't manage user
accounts or profiles. Events are stored in their own `eventa_events` table,
so Eventa never touches your application's existing models or migrations.

## Storage

Any SQLAlchemy connection URL works:

```python
analytics = Analytics(database="sqlite:///eventa.db")
```

SQLite is supported today; other SQL databases (e.g. PostgreSQL) work through
the same mechanism once tested and documented.

## Development

```bash
uv sync --extra dev
uv run pytest
uv run ruff check .
uv run mypy
```

## License

MIT
