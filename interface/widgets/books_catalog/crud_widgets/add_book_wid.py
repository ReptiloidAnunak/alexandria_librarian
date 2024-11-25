

from textual.app import ComposeResult
from textual.widgets import Button, Label, Input, Select
from textual.containers import HorizontalGroup, Vertical
from textual import on
from data_base.models import Book, BookStatus
from interface.widgets.catalog_wids.buttons.buttons_ok import ButtonOkAddBook

class BookAddWidget(HorizontalGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.btn_ok_add_book = ButtonOkAddBook()

        self.input_title = Input(placeholder='Title', type='text')
        self.input_author = Input(placeholder='Autor', type='text')
        self.input_year = Input(placeholder='Year', type='integer')
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Add book:"),
                    self.input_title,
                    self.input_author,
                    self.input_year,

        )
        yield self.btn_ok_add_book
        self.app.logs.info('ADD_BOOKS_WIDGET :: composed')

    @on(ButtonOkAddBook.Pressed)
    def add_book(self, event: ButtonOkAddBook.Pressed):
        button = event.button
        self.app.logs.info(f'BUTTON pressed id: {button.id}')

        if event.button.id == self.btn_ok_add_book.id:
            button.disabled = False
            self.app.logs.info('self.app.db_manager.add_book_to_db()')
            title = self.input_title.value
            self.input_title.value = ''
            self.app.logs.info(f"ADD_BOOK_INPUT :: title: {title}")
            author = self.input_author.value
            self.input_author.value = ''
            self.app.logs.info(f"ADD_BOOK_INPUT :: author: {author}")
            year = self.input_year.value
            self.input_year.value = ''
            if not year:
                year = None
            else:
                year = int(year)
            self.app.logs.info(f"ADD_BOOK_INPUT :: year: {year}")


            book = Book(
                title=title,
                author=author,
                year=year,
                status=BookStatus.available.value
            )
            self.app.db_manager.add_book_to_db(book)
            self.app.logs.info(f"Book :: {book}")
            self.app.books_table.add_row(*book, key=book.id)
            self.app.books_table.show_actual_books_db()
