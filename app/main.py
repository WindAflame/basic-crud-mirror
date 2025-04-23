from fastapi import FastAPI, Body

import datastore as DATASTORE
from models.book import Book

DATASTORE.initialise()

app = FastAPI()


@app.post('/books/create_book')
async def create_book(new_book: Book):
    DATASTORE.BOOKS.append(new_book)


@app.get('/books')
async def read_all_books() -> list[Book]:
    return DATASTORE.BOOKS


@app.put('/books/update_book')
async def update_book(update_book: Book) -> Book | None:
    book_index = next((index for index, b in enumerate(DATASTORE.BOOKS) if b.title.casefold() == update_book.title.casefold()), None)
    if book_index != None:
        DATASTORE.BOOKS[book_index] = update_book
        return update_book
    return None


@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str) -> int:
    book_index = next((index for index, b in enumerate(DATASTORE.BOOKS) if b.title.casefold() == book_title.casefold()), None)
    if book_index != None:
        DATASTORE.BOOKS.pop(book_index)
        return 1
    return 0
