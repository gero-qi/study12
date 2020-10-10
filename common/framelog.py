import logging
import time

from common.function import project_path


class Framelog():
    def __int__(self, logger=None):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.log_time = time.strftime("%Y-%m-%d, %H:%M:%S")
        self.log_path = project_path() + "/Logs/"
        self.log_name = self.log_path+self.log_time+'log.log'
        print(self.log_name)
        fh = logging.FileHandler(self.log_name)
        fh.setLevel(logging.INFO)

        formatter =   logging.Formatter