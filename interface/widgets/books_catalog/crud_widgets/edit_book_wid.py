

from textual.app import ComposeResult
from textual.widgets import Button, Label, Input, Select
from textual.containers import HorizontalGroup, Vertical
from textual import on
from data_base.models import BookStatus
from interface.widgets.catalog_wids.buttons.buttons_ok import ButtonOkEditBook


class EditBookStatusWidget(HorizontalGroup):
    books_status_lst = [BookStatus.available.value, BookStatus.issued.value]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_book_id = Input(placeholder='123456789', type='integer')
        self.select_status = Select([(line, line) for line in self.books_status_lst], prompt='Select book`s status')
        self.btn_ok_status_book = ButtonOkEditBook()

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Change book`s status:"),
        )
        yield Vertical(self.input_book_id,
                       self.select_status,
                       self.btn_ok_status_book)
    @on(ButtonOkEditBook.Pressed)
    def edit_book_status(self, event: Button.Pressed):
        if event.button.id == 'bth_ok_status_book_wid':
            try:
                book_id = int(self.input_book_id.value)
            except ValueError:
                self.app.logs.info(f'EDIT BOOK: ERROR INPUT')
                return
            status = self.select_status.value
            self.app.logs.info(f'EDIT BOOK: {book_id} {status}')
            self.app.db_manager.change_book_status(book_id, status)
            self.app.books_table.show_actual_books_db()
            self.app.books_table.show_actual_books_db()
