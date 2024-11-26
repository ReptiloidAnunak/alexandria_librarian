import logging
import os.path
import subprocess
import time
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import VerticalGroup
from textual.widgets import Log


from data_base.management.base_manager import BaseManager
from interface.widgets.books_catalog.books_catalog import BooksCatalog
from interface.widgets.data_tables import BooksDataTable
from interface.widgets.loaders_checkboxes_group import LoadersCheckboxGroup
from logger_app.loggers.interface_logger import create_interface_logger
from loaders_api.load_files.openlibrary_books_loader import load_openlibrary_books_info


class MainMenu(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield Button("Books Catalog", id='btn_books_catalog', variant='primary')
        yield Button("Load books by API", id='btn_books_load_api', variant='primary')
        yield Button("Quit", id='quit_app', variant='primary')
        self.app.logs.info('MAIN_MENU :: composed')


class AlexLibraryApp(App):
    AUTO_FOCUS = Button
    CSS_PATH = os.path.join('interface', 'static', 'style.tcss')
    name: str = 'Alexandria Library'
    db_manager: BaseManager = BaseManager()
    books_table: BooksDataTable = BooksDataTable()
    active_loaders_paths: list = []


    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
                ("m", "main_menu", "Main Menu")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logs: logging.LoggerAdapter = create_interface_logger()
        self.logs_interface: Log = Log()
        self.main_menu: MainMenu = MainMenu(id="main_menu_container", classes="main_menu_buttons")
        self.loaders_checkgroup: LoadersCheckboxGroup = LoadersCheckboxGroup()
        self.btn_run_books_load_api: Button = Button('Run loading by API', id='btn_run_load_by_api')

    def compose(self) -> ComposeResult:
        """Yield child widgets for a container.
        This method should be implemented in a subclass.
        """
        yield Header(name=self.name)
        yield Footer()
        yield self.main_menu
        self.logs.info("APP INTERFACE COMPOSED")

    def on_button_pressed(self, event: Button.Pressed):
        """Handle button press events of MainMenu"""
        self.logs.info(f'BUTTON pressed :: {event.button.id}')
        if event.button.id == 'btn_books_catalog':
            self.books_table.show_actual_books_db()
            self.main_menu.remove()
            self.mount(BooksCatalog())

        elif event.button.id == 'btn_books_load_api':
            self.main_menu.remove()
            self.mount(self.loaders_checkgroup)
            self.mount(self.btn_run_books_load_api)

        elif event.button.id == 'btn_run_load_by_api':
            self.loaders_checkgroup.remove()
            self.btn_run_books_load_api.remove()
            self.app.logs.info(f"active_loaders_paths : {self.app.active_loaders_paths}")
            load_openlibrary_books_info(self.db_manager)
            self.mount(Static('Books have been loaded by API'))
            time.sleep(2)
            self.mount(self.main_menu)

        elif event.button.id == 'quit_app':
            self.exit()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_main_menu(self) -> None:
        """An action to show main menu"""
        self.mount(self.main_menu)


if __name__ == "__main__":
    # subprocess.run(['python3',  '-m', 'pytest'])
    app = AlexLibraryApp()
    app.run()
