import json
import os

import logging

from .StatusMonitor import StatusMonitor
from .DispatcherManager import DispatcherManager


class SchoolTracker(object):

    def __init__(self, log_level: logging.INFO):
        logging.basicConfig(format="{%(asctime)s} (%(name)s) [%(levelname)s]: %(message)s",
                            datefmt="%x, %X",
                            level=log_level)
        self.logger = logging.getLogger("SchoolTracker")
        self.logger.debug("Creating DispatcherManager...")
        self.DispatcherManager = DispatcherManager()
        self.logger.debug("Loading schools...")
        if os.path.isfile(os.path.join(os.getcwd(), "schools.json")):
            with open(os.path.join(os.getcwd(), "schools.json"), "r") as f:
                schools = json.load(f)
        else:
            self.logger.error("schools.json not found, creating...")
            schools = []
            with open(os.path.join(os.getcwd(), "schools.json"), "w") as f:
                json.dump(schools, f)
        self.logger.debug("Creating StatusMonitor...")
        self.StatusMonitor = StatusMonitor(self.DispatcherManager, schools)

    def start(self):
        self.logger.info("Starting StatusMonitor...")
        self.StatusMonitor.start()
