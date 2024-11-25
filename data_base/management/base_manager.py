import json
import logging
import os
import uuid
from json import JSONDecodeError
from typing import List, Union
from data_base.management.functions import load_book_obj_from_db
from data_base.models import Book, BookStatus
from settings import DB_ABSPATH, ISBN_JSON_PATH
from logger_app.loggers.alex_lib_logger import create_alex_lib_logger


class BaseManager:
    def __init__(self):
        self.name: str = 'Base_Manager'
        self.data_base_path: str = DB_ABSPATH
        self.isbn_paths_lst: str = ISBN_JSON_PATH
        self.logger: logging.LoggerAdapter = create_alex_lib_logger(self.name)

    def create_json_db(self) -> None:
        """Создание JSON-базы данных с отступами, если она отсутствует."""
        if not os.path.exists(self.data_base_path):
            with open(self.data_base_path, 'w', encoding='utf-8') as file:
                json.dump([], file, indent=4, ensure_ascii=False)  # База — список книг
            self.logger.info('Data base has been created')
        else:
            self.logger.info(f'Data base already exists: {self.data_base_path}')

    def get_books_db_data_list(self) -> List[dict]:
        """Открытие базы данных и загрузка содержимого."""
        try:
            with open(self.data_base_path, 'r', encoding='utf-8') as file:
                db_content = json.load(file)
                return db_content

        except (JSONDecodeError, FileNotFoundError):
            self.create_json_db()
            return []

    def get_isbn_data_base_lst(self) -> list:
        try:
            books_db_list = self.get_books_db_data_list()
            isbn_db_lst = [book_dict['isbn'] for book_dict in books_db_list]
            if isbn_db_lst:
                return list(set(isbn_db_lst))
            else: return []

        except (JSONDecodeError, FileNotFoundError):
            self.create_json_db()

    def get_isbn_search_lst(self) -> List[int]:
        """Открытие базы данных и загрузка содержимого."""
        try:
            with open(self.isbn_paths_lst, 'r', encoding='utf-8') as file:
                db_content_row = json.load(file)
                db_content = [int(isbn) for isbn in db_content_row]
                return db_content

        except (JSONDecodeError, FileNotFoundError):
            self.create_json_db()

    def add_book_to_db(self, book: Book) -> None:
        self.logger.info(f'Adding book (id={book.id})', )
        """Добавление книги в базу данных."""
        db_content = self.get_books_db_data_list()
        if not db_content:
            db_content = list()
        if not book.id:
            book.id = str(uuid.uuid4())

        db_content.append(book.to_dict())

        with open(self.data_base_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(db_content, indent=4, ensure_ascii=False))

        self.logger.info(f'\n______________________________'
                         f'\nBook {book.__str__()} has been added to data base')

    def get_book_by_id(self, book_id: int) -> Union[None, Book]:
        books_db_all = self.get_books_db_data_list()
        try:
            book_data = [book for book in books_db_all if book['id'] == book_id][0]
            book = load_book_obj_from_db(book_data)
            return book
        except IndexError:
            self.logger.info(f'GET BOOK BY ID ERROR: no such book (id={book_id})')
            return None

    def get_books_by_title(self, book_title: str) -> Union[None, List[Book]]:
        books_db_all = self.get_books_db_data_list()
        try:
            book_data = [book for book in books_db_all if book['title'] == book_title]
            books_obj_lst = [load_book_obj_from_db(book) for book in book_data]
            return books_obj_lst
        except IndexError:
            self.logger.info(f'GET BOOK BY ID ERROR: no such book (title={book_title})')
            return []

    def get_books_by_author(self, book_author: str) -> Union[None, List[Book]]:
        books_db_all = self.get_books_db_data_list()
        try:
            book_data = [book for book in books_db_all if book['author'] == book_author]
            books_obj_lst = [load_book_obj_from_db(book) for book in book_data]
            return books_obj_lst
        except IndexError:
            self.logger.info(f'GET BOOK BY ID ERROR: no such book (author={book_author})')
            return []

    def get_books_by_year(self, book_year: Union[int, str, None]) -> Union[None, List[Book]]:
        if not book_year:
            return []
        else:
            book_year = int(book_year)
        books_db_all = self.get_books_db_data_list()
        try:
            book_data = [book for book in books_db_all if book['year'] == book_year]
            books_obj_lst = [load_book_obj_from_db(book) for book in book_data]
            return books_obj_lst
        except IndexError:
            self.logger.info(f'GET BOOK BY ID ERROR: no such book (year={book_year})')
            return []

    def delete_book_by_id(self, book_id: int) -> None:
        books_db_all = self.get_books_db_data_list()
        try:
            book_data = [book for book in books_db_all if book['id'] == book_id][0]
        except IndexError:
            self.logger.info(f'DELETE ERROR: no such book (id={book_id})')
            return
        books_db_all.remove(book_data)
        with open(self.data_base_path, 'w', encoding='utf-8') as file:
            json.dump(books_db_all, file, indent=4, ensure_ascii=False)
        self.logger.info(f'Book deleted: {book_data}')


    def load_books_objs_from_db(self) -> List[Book]:
        books_db_list = self.get_books_db_data_list()
        self.logger.info(f"books_db_list: {books_db_list}")
        books_objs_lst = []
        for book_data in books_db_list:
            book = load_book_obj_from_db(book_data)
            books_objs_lst.append(book)
        return books_objs_lst

    def change_book_status(self, book_id: int, status: str) -> None:
        book = self.get_book_by_id(book_id)
        if not book:
            self.logger.info(f'CHANGE STATUS ERROR: no such book (id={book_id})')
            return
        self.logger.info(f"CHANGE STATUS: book (id={book_id}) > {status}")
        book.status = status
        self.delete_book_by_id(book_id)
        self.add_book_to_db(book)

    def get_books_rows(self):
        all_books = self.get_books_db_data_list()
        books_rows = [tuple(book.values()) for book in all_books]
        return books_rows


#
# base_manager = BaseManager()
# print(base_manager.get_books_rows())