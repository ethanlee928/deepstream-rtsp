from abc import ABC, abstractmethod
import gi

gi.require_version("Gst", "1.0")
gi.require_version("GstRtsp", "1.0")
gi.require_version("GstRtspServer", "1.0")
from gi.repository import Gst, GstRtspServer

Gst.init(None)


from pipeline import logger


class RTSPServer(ABC):
    def __init__(self, port: int, endpoint: str) -> None:
        self.port = port
        self.endpoint = endpoint

        self.server = GstRtspServer.RTSPServer.new()
        self.server.set_property("service", str(port))
        self.server.attach(None)
        self.media_factory = GstRtspServer.RTSPMediaFactory.new()

        logger.info("Initialized RTSP server")

    @abstractmethod
    def start(self):
        ...
