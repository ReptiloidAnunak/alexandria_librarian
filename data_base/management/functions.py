from data_base.models import Book
from settings import LOADERS_LST


def load_book_obj_from_db(book_data: dict) -> Book:
    book = Book(
        id=book_data['id'],
        title=book_data['title'],
        author=book_data['author'],
        year=book_data['year'],
        status=book_data['status'],
        isbn=book_data['isbn']
    )
    return book