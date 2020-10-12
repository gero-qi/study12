import logging
import time

from common.function import project_path


class Framelog():

    def __init__(self, logger=None):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.log_time = time.strftime("%Y_%m_%d_")
        self.log_path = project_path() + "/logs/"
        print(self.log_path)
        self.log_name = self.log_path + self.log_time + 'log.log'
        print(self.log_name)
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(name)s - %(funcName)s [line：%(lineno)d]-> %(message)s',
                                      '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        #self.logger.removeHandler(fh)
        fh.close()

    def log(self):
        return self.logger


if __name__ == '__main__':
    lo = Framelog()
    log = lo.log()
    log.error("error")
    #log.debug("debug")
    #log.info("info")
    #log.critical("严重")
