
from textual.app import ComposeResult
from textual.scroll_view import ScrollView
from textual.widget import Widget
from textual.widgets import Button, Label, DataTable
from textual.containers import VerticalGroup, HorizontalGroup
from data_base.management.base_manager import BaseManager
from data_base.models import Book
from interface.widgets.books_load_api_wids.load_by_api_wid import LoadBooksApiWid
from interface.widgets.change_catalog_wids import DeleteBookWidget, AddBookWidget, FindBookWidget, EditBookStatusWidget


class ChangeCatalogWidget(HorizontalGroup):

    def compose(self) -> ComposeResult:
        yield Button('Add book', id='btn_add_book')
        yield Button('Find book', id='btn_find_book')
        yield Button('Edit status', id='btn_edit_book_status')
        yield Button('Delete book', id='btn_del_book')


class BooksCatalog(VerticalGroup):
    base_manager = BaseManager()
    WIDGET_RUNNING: Widget = None
    WIDGET_RUNNING_OK: Button = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns = tuple(Book.model_fields)
        self.rows = self.base_manager.get_books_rows()
        # self.table = self.app.books_table
        self.app.books_table.add_columns(*self.columns)
        self.app.books_table.add_rows(self.rows)
        self.add_book_widget = AddBookWidget()
        self.edit_book_status = EditBookStatusWidget()
        self.del_book_widget = DeleteBookWidget()
        self.find_book_widget = FindBookWidget()

        self.load_books_by_api_widget = LoadBooksApiWid()



    def compose(self) -> ComposeResult:
        yield Label('BOOKS CATALOG')
        yield self.app.books_table
        yield Label('DATABASE MANAGEMENT')
        yield ChangeCatalogWidget()

    def on_button_pressed(self, event: Button.Pressed):
        self.app.logs.info(f'BUTTON pressed id :: {event.button.id}')
        if self.WIDGET_RUNNING:
            self.WIDGET_RUNNING.remove()
        if self.WIDGET_RUNNING_OK:
            self.WIDGET_RUNNING_OK.remove()

        if event.button.id == 'btn_add_book':
            self.app.books_table.show_actual_books_db()
            self.WIDGET_RUNNING = self.add_book_widget
            self.mount(self.add_book_widget)

        elif event.button.id == 'btn_edit_book_status':
            self.app.books_table.show_actual_books_db()
            self.WIDGET_RUNNING = self.edit_book_status
            self.mount(self.edit_book_status)

        elif event.button.id == 'btn_find_book':
            self.app.books_table.show_actual_books_db()
            self.WIDGET_RUNNING = self.find_book_widget
            self.mount(self.find_book_widget)

        elif event.button.id == 'btn_del_book':
            self.app.books_table.show_actual_books_db()
            self.WIDGET_RUNNING = self.del_book_widget
            self.mount(self.del_book_widget)

