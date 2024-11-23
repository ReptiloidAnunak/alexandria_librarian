
from textual.app import ComposeResult
from textual.widgets import Button, Label, Input
from textual.containers import HorizontalGroup, Vertical

from data_base.models import Book


class AddBookWidget(HorizontalGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.btn_ok_add_book = Button('✅', id='bth_ok_add_book_wid', variant="success")

        self.input_title = Input(placeholder='Title', type='text')
        self.input_author = Input(placeholder='Autor', type='text')
        self.input_year = Input(placeholder='Year', type='integer')
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Add book:"),
                    self.input_title,
                    self.input_author,
                    self.input_year,
                    self.btn_ok_add_book
        )
        self.app.logs.info('ADD_BOOKS_WIDGET :: composed')

    def on_button_pressed(self, event: Button.Pressed):
        self.app.logs.info(f'BUTTON pressed id: {event.button.id}')
        if event.button.id == self.btn_ok_add_book.id:
            self.btn_ok_add_book.disabled = False
            self.app.logs.info('self.app.db_manager.add_book_to_db()')
            title = self.input_title.value
            self.app.logs.info(f"ADD_BOOK_INPUT :: title: {title}")
            author = self.input_author.value
            self.app.logs.info(f"ADD_BOOK_INPUT :: author: {author}")
            year = self.input_year.value
            self.app.logs.info(f"ADD_BOOK_INPUT :: year: {year}")

            book = Book(
                title=title,
                author=author,
                year=int(year),
            )
            self.app.db_manager.add_book_to_db(book)
            self.app.logs.info(f"Book :: {book}")
            self.app.books_table.add_row(*book)
            self.btn_ok_add_book.disabled = False
            self.refresh()
        # elif event.button.id == self.btn.id:

class FindBookWidget(HorizontalGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.btn_ok_find_book = Button('✅', id='bth_ok_find_book_wid', variant="success")
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Search book:"),
                    Input(placeholder='Title', type='text'),
                    Input(placeholder='Autor', type='text'),
                    Input(placeholder='Year', type='integer'),
                    self.btn_ok_find_book
        )


class DeleteBookWidget(HorizontalGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_book_id = Input(placeholder='123456789', type='integer')
        self.btn_ok_del_book = Button('✅', id='bth_ok_del_book_wid', variant="success")
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Delete book by ID:"),
                    self.input_book_id,
                    self.btn_ok_del_book

        )

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == self.btn_ok_del_book.id:
            self.app.logs.info('DELETE BOOOK ')
            book_id = self.input_book_id.value

            books_table_rows = self.app.books_table
            self.app.logs.info(books_table_rows)

            # self.app.books_table.remove()
            self.app.db_manager.delete_book_by_id(book_id)
