from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Optional
import math


class TaskState(Enum):
    ACTIVE = "active"
    DELEGATED = "delegated"
    COMPLETED = "completed"
    CANCELED = "canceled"


@dataclass(frozen=True)
class Task:
    id: str
    title: str
    owner: str
    state: TaskState = TaskState.ACTIVE
    delegate: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass(frozen=True)
class TimeEntry:
    task_id: str
    entry_date: date
    minutes: int
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        if self.minutes <= 0:
            raise ValueError("Time entry must be positive")


@dataclass(frozen=True)
class DailyTaskSnapshot:
    task_id: str
    snapshot_date: date
    state: TaskState
    delegate: Optional[str] = None
