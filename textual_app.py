import os.path

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button
from textual.containers import VerticalGroup
from data_base.management.base_manager import BaseManager
from interface.widgets.books_catalog import BooksCatalog, BooksDataTable
from logger_app.loggers.interface_logger import create_interface_logger


class MainMenu(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield Button("Books Catalog", id='btn_books_catalog')
        yield Button("Load books by API", id='btn_books_load_api')
        yield Button("Quit", id='quit_app')
        self.app.logs.info('MAIN_MENU :: composed')


class AlexLibraryApp(App):
    CSS_PATH = os.path.join('interface', 'static', 'style.tcss')
    name = 'Alexandria Library'
    db_manager = BaseManager()
    books_table = BooksDataTable()

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
                ("m", "main_menu", "Main Menu")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logs = create_interface_logger()
        self.main_menu = MainMenu(id="main_menu_container", classes="main_menu_buttons")

    def compose(self) -> ComposeResult:
        yield Header(name=self.name)
        yield Footer()
        yield self.main_menu
        self.logs.info("APP INTERFACE COMPOSED")

    def on_button_pressed(self, event: Button.Pressed):
        self.logs.info(f'BUTTON pressed :: {event.button.id}')
        if event.button.id == 'btn_books_catalog':
            self.books_table.show_actual_books_db()
            self.main_menu.remove()
            self.mount(BooksCatalog())

        elif event.button.id == 'btn_books_load_api':
            # self.books_table.show_actual_books_db()
            self.main_menu.remove()
        elif event.button.id == 'quit_app':
            self.exit()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_main_menu(self) -> None:
        self.mount(self.main_menu)


if __name__ == "__main__":
    app = AlexLibraryApp()
    app.run()
