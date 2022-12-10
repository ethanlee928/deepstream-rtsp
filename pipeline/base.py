import sys
from abc import ABC, abstractmethod
from typing import Optional

import gi

gi.require_version("Gst", "1.0")
gi.require_version("GLib", "2.0")
from gi.repository import Gst, GObject

from utils import get_logger


logger = get_logger("Gstreamer")


class PipelineBase(ABC):
    def __init__(self, name: Optional[str]) -> None:
        Gst.init(sys.argv[1:])
        self.pipeline = Gst.Pipeline.new(name)
        self.loop = GObject.MainLoop()

    def start(self):
        try:
            self.create_pipeline()
            bus = self.pipeline.get_bus()
            bus.add_signal_watch()
            bus.connect("message::eos", self._terminate)
            bus.connect("message::error", self._terminate)
            self.pipeline.set_state(Gst.State.PLAYING)
            self.loop.run()
        except KeyboardInterrupt:
            logger.warning("Exiting")
        except Exception as err:
            logger.error(f"Pipeline error: {err}")

    @abstractmethod
    def create_pipeline(self):
        ...

    def _terminate(self, bus, message):
        if message.type == 2:
            logger.error(f"Pipeline Error from {message.src}, stopping pipeline")
        elif message.type == 4:
            logger.warning(f"Pipeline Warning from {message.src}, stopping pipeline")
        self.pipeline.set_state(Gst.State.NULL)
        self.loop.quit()
