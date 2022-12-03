from typing import Literal

import gi

gi.require_version("Gst", "1.0")
gi.require_version("GstRtsp", "1.0")
gi.require_version("GstRtspServer", "1.0")
from gi.repository import GLib, GObject, Gst, GstRtsp, GstRtspServer

Gst.init(None)


from pipeline import logger


class RTSPServer:
    def __init__(
        self, port: int, endpoint: str, codec: Literal["h264", "h265"]
    ) -> None:
        self.port = port
        self.endpoint = endpoint
        self.codec = codec

        self.server = GstRtspServer.RTSPServer.new()
        self.server.set_property("service", str(port))
        self.server.attach(None)
        self.media_factory = GstRtspServer.RTSPMediaFactory.new()

        logger.info("Initialized RTSP server")

    def start(self, pipeline: str):
        self.media_factory.set_launch(pipeline)
        self.media_factory.set_shared(True)
        self.server.get_mount_points().add_factory(
            f"/{self.endpoint}", self.media_factory
        )
        logger.info(
            f"RTSP Stream @ rtsp://127.0.0.1:{self.port}/{self.endpoint}"
        )
