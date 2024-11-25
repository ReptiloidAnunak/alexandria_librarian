
from typing import List

from textual.app import App, ComposeResult
from textual.demo.widgets import Checkbox
from textual.widgets import Header, Footer, Button, Static
from textual.containers import VerticalGroup, HorizontalGroup

from backend.loaders_api.loader_api_model import LoaderAPI
from settings import LOADERS_LST



class LoadersCheckboxGroup(VerticalGroup):
    def __init__(self):
        super().__init__()
        self.checkboxes: List[Checkbox] = []
        self.id: str = 'vertical_checkbox_group'

    def compose(self) -> ComposeResult:
        yield Static("Select loader")
        for loader in LOADERS_LST:
            if loader.startswith('loader_') or loader.endswith('_loader.py'):
                checkbox = Checkbox(loader.strip('.py'), id=loader.strip('.py'), value=True)
                self.checkboxes.append(checkbox)
                yield checkbox

    def on_checkbox_changed(self):
        self.app.logs.info(f'CHECKBOXGROUP: {self.id}')
        self.app.logs.info(f"on_checkbox_changed")


        for checkbox in self.checkboxes:
            loader = LoaderAPI(file=(checkbox.id + ".py"),
                active=checkbox.value)
            self.app.logs.info(f"LOADER : {loader}")
            if loader.active and loader.path:
                self.app.active_loaders_paths.append(loader.path)

            elif not loader.active:
                try:
                    self.app.active_loaders_paths.remove(loader.path)
                except ValueError:
                    pass
            self.app.active_loaders_paths = list(set(self.app.active_loaders_paths))
        self.app.logs.info(f"active_loaders_paths : {self.app.active_loaders_paths}")