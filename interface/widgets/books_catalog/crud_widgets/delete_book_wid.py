
from textual.app import ComposeResult
from textual.widgets import Button, Label, Input, Select
from textual.containers import HorizontalGroup, Vertical
from interface.widgets.books_catalog.buttons.buttons_ok import ButtonOkDelBook


class DeleteBookWidget(HorizontalGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_book_id = Input(placeholder='123456789', type='integer')
        self.btn_ok_del_book = ButtonOkDelBook()

    def compose(self) -> ComposeResult:
        """Yield child widgets for a container.
        This method should be implemented in a subclass.
        """
        yield Vertical(
            Label("Delete book by ID:"),
                    self.input_book_id,
                    self.btn_ok_del_book)

    def on_button_pressed(self, event: Button.Pressed):
        """Deletes Book class object to database if rel button has been pressed"""
        if event.button.id == self.btn_ok_del_book.id:
            self.app.logs.info('DELETE BOOK OK')
            try:
                book_id = int(self.input_book_id.value)
                self.input_book_id.value = ''
            except ValueError:
                self.app.logs.info(f'EDIT BOOK: ERROR INPUT')
                return
            self.app.db_manager.delete_book_by_id(int(book_id))
            self.app.books_table.show_actual_books_db()
            self.app.refresh()