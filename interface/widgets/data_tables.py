

from textual.widgets import DataTable
class BooksDataTable(DataTable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = 'data_table_books'
