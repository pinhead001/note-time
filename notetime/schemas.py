from datetime import date
from pydantic import BaseModel, field_validator

# ------------------------------
# Task input
# ------------------------------
class TaskCreate(BaseModel):
    title: str
    priority: int = 3
    project_id: int | None = None

# ------------------------------
# WorkEntry input
# ------------------------------
class WorkEntryCreate(BaseModel):
    task_id: int
    date: date
    minutes: int
    note: str | None = None

    @field_validator("minutes")
    @classmethod
    def positive_minutes(cls, v):
        if v <= 0:
            raise ValueError("Minutes must be positive")
        return v

# ------------------------------
# Task summary output
# ------------------------------
class TaskSummary(BaseModel):
    title: str
    total_minutes: int
