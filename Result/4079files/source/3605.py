import json
import os

import logging

import pushover
import sys

from ..School import School
from .NotificationDispatcher import NotificationDispatcher


class PushoverDispatcher(NotificationDispatcher):

    dispatcher_name = "PUSHOVER"

    def __init__(self):
        self.logger = logging.getLogger("PushoverDispatcher")
        self.logger.debug("Loading Pushover config info...")
        if os.path.isfile(os.path.join(os.getcwd(), "pushover_config.json")):
            with open(os.path.join(os.getcwd(), "pushover_config.json"), "r") as f:
                self.config = json.load(f)
        else:
            self.logger.error("pushover_config.json not found, creating...")
            self.config = {
                "TOKEN": "",
                "USER_KEY": ""
            }
            with open(os.path.join(os.getcwd(), "pushover_config.json"), "w") as f:
                json.dump(self.config, f, indent=4, sort_keys=True)

        try:
            self.logger.debug("Authenticating with Pushover...")
            pushover.init(self.config["TOKEN"])
            self.client = pushover.Client(self.config["USER_KEY"])
            if not self.client.verify():
                self.logger.error("Failed to authenticate with Pushover. Please correct the details in "
                                  "pushover_config.json and restart.")
                sys.exit(1)
            else:
                self.logger.debug("Authenticated with Pushover.")
        except (pushover.InitError, pushover.UserError, pushover.RequestError):
            self.logger.error("Failed to authenticate with Pushover. Please correct the details in "
                              "pushover_config.json and restart.")
            sys.exit(1)

    def dispatch_notification(self, school: School, new_status: str):
        if not os.getenv("SCHOOLTRACKER_DEBUG", False):
            self.client.send_message("New status: {}".format(new_status), title="{} status updated".format(school.name))
