import logging
import logging.handlers

LOG_FILE_ABS_PATH = '/var/log/etsin_finder/reindexing.log'


def get_logger(logger_name):
    logger = logging.getLogger(logger_name if logger_name else 'reindexing')
    _set_info_level_logger(logger)
    return logger


def _set_info_level_logger(logger):
    logger.addHandler(_get_rotating_log_handler('INFO'))


def _set_debug_level_logger(logger):
    logger.addHandler(_get_rotating_log_handler('DEBUG'))


def _get_rotating_log_handler(log_level):
    handler = logging.handlers.RotatingFileHandler(LOG_FILE_ABS_PATH, maxBytes=10000000, mode='a', backupCount=30)
    handler.setLevel(log_level)
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    return handler
