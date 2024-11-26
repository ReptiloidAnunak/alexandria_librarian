import logging

from logger_app.loggers.alex_lib_logger import create_alex_lib_logger


def create_core_logger() -> logging.Logger:
    """Creates core logger"""
    logger_main = create_alex_lib_logger('MAIN_LOG')
    logger_main.info(f'Logger created: {logger_main.logger.name}')
    return logger_main


