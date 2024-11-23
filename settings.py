import os



APP_NAME = 'Alexandria  Librarian'

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# DATA BASE
DB_DIR_NAME = 'data_base'
DB_NAME = 'alexandria_books.json'
DB_ABSPATH = os.path.join(ROOT_DIR, DB_DIR_NAME, DB_NAME)
ISBN_JSON_PATH = os.path.join(ROOT_DIR, DB_DIR_NAME, 'isbn_search_lst.json')

# LOGGING
LOGGER_DIR = os.path.join(ROOT_DIR, 'logger_app')
LOGS_FILENAME = 'alex_lib.log'
LOGS_FILE_ABSPATH = os.path.join(ROOT_DIR, LOGGER_DIR, LOGS_FILENAME)
APP_LOGGER_NAME = 'AlexLibLogger'
MAIN_LOGGER_NAME = 'MAIN_LOG'




