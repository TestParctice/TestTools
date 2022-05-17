# encoding:utf-8
import logging
import time
import os.path


class log(object):

    def logger(self):
        logger = logging.getLogger()
        logger.setLevel("DEBUG")
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + './log_report/'
        log_path = os.path.dirname(os.path.dirname(__file__)) + './log_report/'
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        ch = logging.StreamHandler()
        fm = logging.Formatter('%(asctime)s-%(pathname)s-%(module)s:%(lineno)d-%(levelname)s-%(message)s ')
        fh.setFormatter(fm)
        ch.setFormatter(fm)
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

# logger = log.logger()
# logger.debug("debug")
# logger.info("info")
# logger.warning("warning")
# logger.error("error")
# logger.critical("critical")
