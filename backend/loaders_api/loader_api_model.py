import os

from pydantic import BaseModel

import settings


class LoaderAPI(BaseModel):
    file: str
    path: str = None
    active: bool = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.path = os.path.join(settings.LOADERS_DIR, self.file)

    def __str__(self):
        return f'{self.file} : {self.active}'