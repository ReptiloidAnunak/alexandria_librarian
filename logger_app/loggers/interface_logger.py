from logger_app.loggers.alex_lib_logger import create_alex_lib_logger

logger = create_alex_lib_logger('INTERFACE')


def create_interface_logger():
    """Creates a logger for textual interface"""
    logger = create_alex_lib_logger('INTERFACE')
    return logger

