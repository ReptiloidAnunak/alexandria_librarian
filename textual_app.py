import os.path
from distutils.command.check import check
from tkinter import Label
from tkinter.tix import CheckList
from typing import List
import time
from textual.app import App, ComposeResult
from textual.demo.widgets import Checkbox
from textual.widgets import Header, Footer, Button, Static, LoadingIndicator
from textual.containers import VerticalGroup, HorizontalGroup
import settings
from backend.loaders_api.load_files.openlibrary_books_loader import load_openlibrary_books_info
from backend.loaders_api.loader_api_model import LoaderAPI
from textual.widgets import Log
from data_base.management.base_manager import BaseManager
from interface.widgets.books_catalog import BooksCatalog
from interface.widgets.data_tables import BooksDataTable
from interface.widgets.loaders_checkboxes_group import LoadersCheckboxGroup
from logger_app.loggers.interface_logger import create_interface_logger
from settings import LOADERS_LST



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
    active_loaders_paths = []


    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
                ("m", "main_menu", "Main Menu")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logs = create_interface_logger()
        self.logs_interface = Log()
        self.main_menu = MainMenu(id="main_menu_container", classes="main_menu_buttons")
        self.loaders_checkgroup = LoadersCheckboxGroup()
        self.btn_run_books_load_api = Button('Run loading by API', id='btn_run_load_by_api')

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

            # while True:
            #     self.app.logs.info(f" LOGGER START LOAD API")

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
