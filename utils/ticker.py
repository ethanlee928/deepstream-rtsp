from abc import ABC, abstractmethod
from time import time

from overrides import overrides

from .functions import seconds_between


class Ticker(ABC):
    def __init__(self, interval: float) -> None:
        if not isinstance(interval, (int, float)):
            raise ValueError("Interval must be float")
        self.interval = interval

    @abstractmethod
    def tick(self) -> bool:
        ...


class FPSticker(Ticker):
    def __init__(self, interval: float) -> None:
        super().__init__(interval)
        self.fps = 0
        self.frame_count = 0
        self._time = time()

    @overrides
    def tick(self) -> bool:
        self.frame_count += 1
        now = time()
        delta_t = seconds_between(now, self._time)
        if delta_t > self.interval:
            self.fps = int(self.frame_count / delta_t)
            self.frame_count = 0
            self._time = now
            return True
        return False
