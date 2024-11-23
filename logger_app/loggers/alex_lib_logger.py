
from settings import LOGS_FILE_ABSPATH

import logging
from settings import APP_LOGGER_NAME


def create_alex_lib_logger(loger_special_name: str) -> logging.LoggerAdapter:
    logger = logging.getLogger(APP_LOGGER_NAME)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(LOGS_FILE_ABSPATH, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s :: %(loger_special_name)s >> %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    new_logger = logging.LoggerAdapter(logger, extra={'loger_special_name': loger_special_name})
    return new_logger