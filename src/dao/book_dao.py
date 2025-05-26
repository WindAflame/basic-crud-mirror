from typing import Optional

import datastore as DB
from models.book import Book


class BookDAO(object):

    @property
    def items(self) -> list[Book]:
        return DB.books
    @items.setter
    def items_set(self, books: list[Book]):
        DB.books = books

    def __init__(self):
        pass

    def create(self, item: Book) -> Book:
        
        if item.id is None:
            item.id = len(self.items) + 1
        self.items.append(item)
        return item

    def read(self, item_id: int) -> Optional[Book]:
        return next(item for item in self.items if item['id'] == item_id)

    def read_all(self) -> list[Book]:
        return self.items

    def update(self, item_id: int, item: Book) -> Optional[Book]:
        for index, db_item in enumerate(self.items):
            if db_item == item_id:
                self.items[index] = item
                return item
        return None

    def delete(self, item_id: int) -> bool:
        for index, db_item in enumerate(self.items):
            if db_item == item_id:
                del self.items[index]
                return True
        return False