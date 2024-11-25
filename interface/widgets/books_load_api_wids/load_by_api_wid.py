from textual.app import ComposeResult
from textual.containers import VerticalGroup
from textual.widgets import Checkbox
from settings import LOADERS_LST



class LoadersCheckbox(VerticalGroup):
    self_loaders = LOADERS_LST

    def compose(self) -> ComposeResult:
        for loader in self.self_loaders:
            yield Checkbox(label=loader)




class LoadBooksApiWid(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield LoadersCheckbox()
