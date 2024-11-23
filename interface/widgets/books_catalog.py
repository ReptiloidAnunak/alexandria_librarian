
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Button, Label, DataTable
from textual.containers import VerticalGroup, HorizontalGroup
from data_base.management.base_manager import BaseManager
from data_base.models import Book
from interface.widgets.change_catalog_wids import DeleteBookWidget, AddBookWidget, FindBookWidget
from interface.widgets.data_tables import BooksDataTable


class ChangeCatalogWidget(HorizontalGroup):

    def compose(self) -> ComposeResult:
        yield Button('Add book', id='btn_add_book')
        yield Button('Find book', id='btn_find_book')
        yield Button('Delete book', id='btn_del_book')

class BooksCatalog(VerticalGroup):
    base_manager = BaseManager()
    WIDGET_RUNNING: Widget = None
    WIDGET_RUNNING_OK: Button = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns = tuple(Book.model_fields)
        self.rows = self.base_manager.get_books_rows()
        self.table = self.app.books_table
        self.table.add_columns(*self.columns)
        self.table.add_rows(self.rows)

        self.add_book_widget = AddBookWidget()
        self.del_book_widget = DeleteBookWidget()
        self.find_book_widget = FindBookWidget()


    def compose(self) -> ComposeResult:
        yield Label('BOOKS CATALOG')
        yield self.table
        yield Label('DATABASE MANAGEMENT')
        yield ChangeCatalogWidget()

    def on_button_pressed(self, event: Button.Pressed):
        self.app.logs.info(f'BUTTON pressed id :: {event.button.id}')
        if self.WIDGET_RUNNING:
            self.WIDGET_RUNNING.remove()
        if self.WIDGET_RUNNING_OK:
            self.WIDGET_RUNNING_OK.remove()

        if event.button.id == 'btn_add_book':
            self.WIDGET_RUNNING = self.add_book_widget
            self.mount(self.add_book_widget)

        elif event.button.id == 'btn_find_book':
            self.WIDGET_RUNNING = self.find_book_widget
            self.mount(self.find_book_widget)
        elif event.button.id == 'btn_del_book':
            self.WIDGET_RUNNING = self.del_book_widget
            self.mount(self.del_book_widget)

