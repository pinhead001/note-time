# Notetime

A notebook-style weekly task and time-tracking app.

## Core Concepts
- Tasks are planned intent
- Weeks define planning windows
- Work entries record actual time spent

Tech stack:
- Python
- SQLAlchemy
- Pydantic
- SQLite

How to run
Open CMD/PowerShell in the repo root →
python -m pip install --upgrade pip && pip install sqlalchemy pydantic && python -m notetime.create_db && python -m notetime.seed
