from time import time

from .functions import seconds_between


class FPSticker:
    def __init__(self, interval: float) -> None:
        self.interval = interval
        self.fps = 0
        self.frame_count = 0
        self._time = time()

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
