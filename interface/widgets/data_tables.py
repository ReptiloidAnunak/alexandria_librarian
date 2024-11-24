from typing import List

from textual.widgets import DataTable
from textual.widgets._data_table import DuplicateKey
from data_base.models import Book


class BooksDataTable(DataTable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = 'data_table_books'

    def show_actual_books_db(self):
        self.clear()
        books_objs_upt = self.app.db_manager.load_books_objs_from_db()
        for book in books_objs_upt:
            try:
                self.add_row(*book.to_db_row_tuple(), key=book.id)
            except ValueError as e:
                self.app.logs.info(f"Error args to show_row: {book.to_db_row_tuple()}")

    def show_books_query_result_in_dt(self, books_lst: List[Book]):
        if books_lst:
            self.clear()
            for book in books_lst:
                try:
                    self.add_row(*book.to_db_row_tuple(), key=book.id)
                except DuplicateKey as e:
                   self.app.logs.info(e)

