


from textual.app import ComposeResult
from textual.widgets import Button, Label, Input, Select
from textual.containers import HorizontalGroup, Vertical
from interface.widgets.catalog_wids.buttons.buttons_ok import ButtonOkFindBook


class FindBookWidget(HorizontalGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_title = Input(placeholder='Title', type='text')
        self.input_author = Input(placeholder='Autor', type='text')
        self.input_year = Input(placeholder='Year', type='integer')
        self.btn_ok_find_book = ButtonOkFindBook()

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Search book:"),
                    self.input_title,
                    self.input_author,
                    self.input_year,
        )
        yield self.btn_ok_find_book

    def on_button_pressed(self, event: Button.Pressed):
        self.app.books_table
        if event.button.id == self.btn_ok_find_book.id:
            self.app.logs.info('FIND BOOK OK')
            self.btn_ok_find_book.disabled = False
            self.app.logs.info('self.app.db_manager.add_book_to_db()')

            title = self.input_title.value
            self.input_title.value = ''
            books_by_title = self.app.db_manager.get_books_by_title(title)
            self.app.logs.info(f"FIND_BOOK_INPUT :: title: {title}")
            self.app.logs.info(f"books_by_title {books_by_title}")

            author = self.input_author.value
            self.input_author.value = ''
            books_by_author = self.app.db_manager.get_books_by_author(author)
            self.app.logs.info(f"FIND_BOOK_INPUT :: author: {author}")
            self.app.logs.info(f"FIND_BOOK_INPUT :: books_by_author: {books_by_author}")

            year = self.input_year.value
            self.input_year.value = ''
            books_by_year = self.app.db_manager.get_books_by_year(year)
            self.app.logs.info(f"FIND_BOOK_INPUT :: year: {year}")
            self.app.logs.info(f"FIND_BOOK_INPUT :: books_by_year: {books_by_year}")

            found_not_filtered_books = list(books_by_title + books_by_author + books_by_year)
            self.app.logs.info(f"FIND_BOOK_INPUT :: found_books_not_filtered: {found_not_filtered_books}")

            if title and author:
                result = [book for book in found_not_filtered_books if book.title == title and book.author == author and book.title is not None]
            elif title and year:
                result = [book for book in found_not_filtered_books if book.title == title and book.year == year and str(year).isint()]
            elif author and year:
                result = [book for book in found_not_filtered_books if book.author == author and book.year == year]
            else:
                result = found_not_filtered_books

            self.app.logs.info(f"FIND_BOOK_INPUT :: found_books_filtered: {result}")

            self.app.books_table.show_books_query_result_in_dt(result)