from time import sleep

from faker import Faker
from data_base.models import Book, BookStatus
from data_base.management.base_manager import BaseManager


fake = Faker()
base_manager = BaseManager()


def add_fake_book_to_db():
    book = Book(
        title=fake.word().capitalize(),
        author=f"{fake.first_name()} {fake.name()}",
        year=int(fake.year()),
        status=BookStatus.available.value,
    )
    base_manager.add_book_to_db(book)
    return book


def test_add_book():
    book = add_fake_book_to_db()
    assert book

def test_delete_book():
    book = add_fake_book_to_db()
    book_id = book.id
    base_manager.delete_book_by_id(book_id)
    book = base_manager.get_book_by_id(book_id)
    assert not book


def test_change_book_status():
    book = add_fake_book_to_db()
    print(book)
    book.status = BookStatus.available.value
    id_search = book.id
    base_manager.change_book_status(book_id=id_search,
                                    status=BookStatus.issued.value)
    sleep(0.4)
    book_upt = base_manager.get_book_by_id(id_search)
    print(book_upt)
    print(book_upt.status)
    assert book_upt.status == BookStatus.issued.value

