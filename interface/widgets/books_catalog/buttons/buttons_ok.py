from textual.widgets import Button


class ButtonOkAddBook(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = 'bth_ok_add_book_wid'
        self.label = 'OK'
        self.variant = "success"



class ButtonOkEditBook(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = 'bth_ok_status_book_wid'
        self.label = 'OK'
        self.variant = "success"


class ButtonOkFindBook(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = 'bth_ok_find_book_wid'
        self.label = 'OK'
        self.variant = "success"


class ButtonOkDelBook(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = 'bth_ok_del_book_wid'
        self.label = 'OK'
        self.variant = "success"
