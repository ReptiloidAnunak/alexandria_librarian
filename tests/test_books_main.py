import os
from time import sleep

from faker import Faker
from data_base.models import Book, BookStatus
from data_base.management.base_manager import BaseManager
from settings import TEST_DB_PATH

fake = Faker()
test_base_manager = BaseManager()
test_base_manager.data_base_path = TEST_DB_PATH


def add_fake_book_to_db():
    book = Book(
        title=fake.word().capitalize(),
        author=f"{fake.first_name()} {fake.name()}",
        year=int(fake.year()),
        status=BookStatus.available.value,
    )
    test_base_manager.add_book_to_db(book)
    return book

def test_create_json_db():
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    test_base_manager.create_json_db()
    assert os.path.exists(TEST_DB_PATH)

def test_change_book_status():
    book = add_fake_book_to_db()
    print(book)
    book_status_old = BookStatus.available.value
    id_search = book.id
    test_base_manager.change_book_status(book_id=id_search,
                                         status=BookStatus.issued.value)
    sleep(0.4)
    book_upt = test_base_manager.get_book_by_id(id_search)
    assert book_upt.status != book_status_old

def test_add_book():
    book = add_fake_book_to_db()
    assert book

def test_delete_book():
    book = add_fake_book_to_db()
    book_id = book.id
    test_base_manager.delete_book_by_id(book_id)
    book = test_base_manager.get_book_by_id(book_id)
    assert not book

def test_get_book_by_id():
    book = add_fake_book_to_db()
    book_id = book.id
    test_base_manager.get_book_by_id(book_id)
    book_from_db = test_base_manager.get_book_by_id(book_id)
    assert book_from_db.id == book_id

def test_get_books_by_title():
    book = add_fake_book_to_db()
    book_title = book.title
    books_from_db = test_base_manager.get_books_by_title(book_title)
    result = [book for book in books_from_db]
    assert len(result) > 0

def test_get_books_by_author():
    book = add_fake_book_to_db()
    book_author = book.author
    books_from_db = test_base_manager.get_books_by_author(book_author)
    result = [book for book in books_from_db]
    assert len(result) > 0


def test_get_books_by_year():
    book = add_fake_book_to_db()
    book_year = book.year
    books_from_db = test_base_manager.get_books_by_year(book_year)
    result = [book for book in books_from_db]
    assert len(result) > 0

def test_add_book_to_db():
    book = Book(
        title=fake.word().capitalize(),
        author=f"{fake.first_name()} {fake.name()}",
        year=int(fake.year()),
        status=BookStatus.available.value,
    )
    test_base_manager.add_book_to_db(book)
    book_from_db = test_base_manager.get_book_by_id(book.id)
    assert book_from_db.id == book.id
    assert book_from_db.title == book.title
    assert book_from_db.author == book.author
    assert book_from_db.status == book.status


def test_load_books_objs_from_db():
    books_objs_lst = test_base_manager.load_books_objs_from_db()
    books_data_lst = test_base_manager.get_books_db_data_list()

    assert len(books_data_lst) == len(books_objs_lst)
    assert all(any(book_obj.to_dict() == book_data for book_data in books_data_lst) for book_obj in books_objs_lst)


def test_get_books_rows():
    books_objs_lst = test_base_manager.load_books_objs_from_db()
    books_rows = test_base_manager.get_books_rows()
    assert len(books_objs_lst) == len(books_objs_lst)
    assert all(any(book_obj.to_db_row_tuple() == book_data for book_data in books_rows) for book_obj in books_objs_lst)






