import sys
from abc import ABC, abstractmethod
from typing import Optional

import gi

gi.require_version("Gst", "1.0")
gi.require_version("GLib", "2.0")
from gi.repository import Gst, GObject


class PipelineBase(ABC):
    def __init__(self, name: Optional[str]) -> None:
        Gst.init(sys.argv[1:])
        self.pipeline = Gst.Pipeline.new(name)
        self.loop = GObject.MainLoop()

    @abstractmethod
    def create_pipeline(self):
        ...
