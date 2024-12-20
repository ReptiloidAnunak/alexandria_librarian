import json
import re
from http.client import responses
from time import sleep
import requests
from data_base.management.base_manager import BaseManager
from data_base.models import Book, BookStatus
from logger_app.loggers.alex_lib_logger import create_alex_lib_logger

openlibrary_loader_log = create_alex_lib_logger("Open Library Loader")

def load_openlibrary_books_info(base_manager: BaseManager) -> None:
    """Loads books api from https://openlibrary.org into json database"""
    openlibrary_loader_log.info(f'Running')
    isbn_data_base_lst = base_manager.get_isbn_data_base_lst()
    openlibrary_loader_log.info(f'isbn_data_base_lst: {isbn_data_base_lst}')
    isbn_lst_from_search_lst_json = base_manager.get_isbn_search_lst()
    openlibrary_loader_log.info(f'isbn_lst_from_search_lst_json: {isbn_lst_from_search_lst_json}')
    result_raw = [isbn if int(isbn) not in isbn_data_base_lst else openlibrary_loader_log.info(f'ISBN {isbn} :: Already in data_base') for isbn in isbn_lst_from_search_lst_json]
    isbn_lst = list(set(result_raw))
    openlibrary_loader_log.info(f'isbn_lst: {isbn_lst}')

    for isbn in isbn_lst:
        if isbn in base_manager.get_isbn_data_base_lst():
            openlibrary_loader_log.info(f'Already in Data Base: isbn {isbn}')
        else:
            api_url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
            try:
                response = requests.get(api_url)
            except requests.exceptions.ConnectionError as e:
                openlibrary_loader_log.critical(e)
                sleep(2)
                response = requests.get(api_url)
            openlibrary_loader_log.info(f'API RESPONSE: isbn {isbn} :: {response}\n{api_url}\n')

            if response.status_code == 200:
                data = response.json()
                print(data)
                if data:
                    book_data_dict = list(data.values())[0]
                    title = book_data_dict["title"]
                    try:
                        authors = book_data_dict['authors']
                    except KeyError:
                        authors = []
                    authors_names_lst = [author['name'] for author in authors]
                    author_st = '; '.join(authors_names_lst)
                    year_str = re.search(r'(\d\d\d\d)', book_data_dict['publish_date'])
                    year = int(year_str.group(0))

                    book = Book(title=title, author=author_st,year=year, status=BookStatus.available.value, isbn=isbn)
                    base_manager.add_book_to_db(book)

    #

if __name__ == "__main__":
    base_manager = BaseManager()
    load_openlibrary_books_info(base_manager)