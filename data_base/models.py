
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
    year: Union[int, None]
    status: Union[str, None]
    isbn: Union[None, int] = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id', random.randint(1, 99999))

    def to_dict(self):
        """Converts Book class`s object to dictionary"""
        return dict(id=self.id,
                    title=self.title,
                    author=self.author,
                    year=self.year,
                    status=self.status,
                    isbn=self.isbn)

    def to_db_row_tuple(self):
        """Converts Book class`s object to tuple"""
        return tuple([self.id, self.title, self.author, self.year, self.status, self.isbn])

    def __str__(self):
        return ('\n'
                f'№ {self.id}\n'
                f'Автор: {self.author}\n'
                f'Название: {self.title}\n'
                f'Год: {self.year}\n'
                f'Статус: {self.status}\n'
                f'~~~~~~~~~\n')
