from data_base.models import Book


def load_book_obj_from_db(book_data: dict) -> Book:
    book = Book(
        id=book_data['id'],
        title=book_data['title'],
        author=book_data['author'],
        year=book_data['year'],
        isbn=book_data['isbn']
    )
    return book