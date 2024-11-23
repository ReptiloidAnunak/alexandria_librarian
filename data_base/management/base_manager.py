import json
import os.path
from settings import DB_ABSPATH
from app_logger.create_alex_lib_logger import create_alex_lib_logger


class BaseManager:
    def __init__(self):
        self.name = 'Base_Manager'
        self.data_base = DB_ABSPATH
        self.logger = create_alex_lib_logger(self.name)

    def create_json_db(self) -> None:
        if not os.path.exists(self.data_base):
            with open(self.data_base, 'w+') as file:
                file.write(json.dumps({}))
        else:
            self.logger.info(f'DB already exists')


    def open_json_db(self):
        if not os.path.exists(self.data_base):
            self.create_json_db()

        with open(self.data_base, 'r') as file:
            db_content = json.loads(file.read())
            print(db_content)