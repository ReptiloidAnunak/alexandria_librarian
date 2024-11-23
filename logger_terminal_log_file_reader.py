import time
from logger_app.loggers.core_logger import create_core_logger
from settings import LOGS_FILE_ABSPATH

class LogsFileTerminalReader:

    def __init__(self):
        self.logger = create_core_logger()
        self.read_logs_with_interface()
        self.logger.info('RUNNING: LogsFileTerminalReader')

    def read_logs_with_interface(self):
        with open(LOGS_FILE_ABSPATH, 'r') as file:
            print(file.read())
            file.seek(0, 2)
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.5)
                    continue
                print(line, end="")


if __name__ == "__main__":
    logs_reader = LogsFileTerminalReader()