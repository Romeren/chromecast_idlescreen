"""
Controller to interface with the Plex-app.
"""
from pychromecast.controllers import BaseController

MESSAGE_TYPE = 'type'

TYPE_PLAY = "PLAY"
TYPE_PAUSE = "PAUSE"
TYPE_STOP = "STOP"


class DashboardController(BaseController):
    """Controller to interact with namespace. """

    def __init__(self, start_url):
        super(DashboardController, self).__init__(
            "urn:x-cast:dashboard.com.framework", "F6EF1BA7")
        self.start_url = start_url

    def stop(self):
        """Send stop command. """
        self.send_message({MESSAGE_TYPE: TYPE_STOP})

    def pause(self):
        """Send pause command. """
        self.send_message({MESSAGE_TYPE: TYPE_PAUSE})

    def play(self):
        """Send play command. """
        self.send_message({MESSAGE_TYPE: TYPE_PLAY})

    def on_app_start(self):
        self.send_msg({'url': self.start_url})

    def send_msg(self, message):
        self.send_message(message)
