from typing import overload
from datetime import datetime


@overload
def seconds_between(time1: float, time2: float) -> float:
    ...


@overload
def seconds_between(time1: datetime, time2: datetime) -> float:
    ...


def seconds_between(time1: datetime, time2: datetime) -> float:
    if isinstance(time1, (int, float)) and isinstance(time2, (int, float)):
        return abs(time1 - time2)
    elif isinstance(time1, datetime) and isinstance(time2, datetime):
        return abs((time1 - time2).total_seconds())
    else:
        raise ValueError("Unsupported input type")
