
from enum import Enum
import random

from pydantic import BaseModel
from typing import Union


class BookStatus(Enum):
    available = 'в наличии'
    issued = 'выдана'


class Book(BaseModel):
    id: Union[None, int] = None
    title: str
    author: Union[str, None]
    year: int
    status: str = BookStatus.available.value
    isbn: Union[None, int] = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id', random.randint(1, 99999))

    def to_dict(self):
        return dict(id=self.id,
                    title=self.title,
                    author=self.author,
                    year=self.year,
                    status=self.status,
                    isbn=self.isbn)

    def __str__(self):
        return ('\n'
                f'№ {self.id}\n'
                f'Автор: {self.author}\n'
                f'Название: {self.title}\n'
                f'Год: {self.year}\n'
                f'Статус: {self.status}\n'
                f'~~~~~~~~~\n')
