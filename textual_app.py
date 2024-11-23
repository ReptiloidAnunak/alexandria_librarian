
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label, DataTable
from textual.containers import VerticalGroup

from data_base.management.base_manager import BaseManager


class BooksDataTable(DataTable):
    column_names = []
    ROWS = [
        ("lane", "swimmer", "country", "time"),
        (4, "Joseph Schooling", "Singapore", 50.39),
        (2, "Michael Phelps", "United States", 51.14),
        (5, "Chad le Clos", "South Africa", 51.14),
        (6, "László Cseh", "Hungary", 51.14),
        (3, "Li Zhuhao", "China", 51.26),
        (8, "Mehdy Metella", "France", 51.58),
        (7, "Tom Shields", "United States", 51.73),
        (1, "Aleksandr Sadovnikov", "Russia", 51.84),
        (10, "Darren Burns", "Scotland", 51.84),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_columns(*self.ROWS[0])
        self.add_rows(self.ROWS[1:])


class BooksCatalog(VerticalGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    def compose(self) -> ComposeResult:
        yield Label('Books Catalog')
        yield BooksDataTable()


class MainMenu(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield Button("Books Catalog", id='btn_books_catalog')
        yield Button("Load books by API", id='btn_books_load_api')
        yield Button("Quit", id='quit_app')


class AlexLibraryApp(App):
    CSS_PATH = 'static/style.tcss'
    name = 'Alexandria Library'

    db_manager = BaseManager()

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
                ("m", "main_menu", "Main Menu")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_menu = MainMenu(id="main_menu_container", classes="main_menu_buttons")


    def compose(self) -> ComposeResult:
        yield Header(name=self.name)
        yield Footer()
        yield self.main_menu

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == 'btn_books_catalog':
            self.main_menu.remove()
            self.mount(BooksCatalog())

        elif event.button.id == 'btn_books_load_api':
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
