import json
from flask import request
from flask_restx import Namespace, Resource

import datastore
from models.book import Book
from models.api_models import book_model

ns = Namespace('books', description='Manage a bookstore')


@ns.route('/', endpoint='')
class BooksGETResource(Resource):
    @ns.marshal_list_with(book_model)
    def get(self):
        return datastore.books, 200


@ns.route('/create_book', endpoint='create_book')
class BooksPOSTResource(Resource):
    @ns.expect(book_model)
    def post(self):
        book = json.loads(request.data)
        _check_required_fields(book, ['title', 'author', 'category'])
        datastore.books.append(book)
        return book, 200


@ns.route('/update_book', endpoint='update_book')
class BooksPUTResource(Resource):
    @ns.expect(book_model)
    def put(self):
        book = json.loads(request.data)
        _check_required_fields(book, ['title', 'author', 'category'])
        book_obj = Book(**book)
        book_finded, book_index = _find_book_in_bookstore(book_obj)
        book_finded_obj = Book(**book_finded)
        book_finded_obj.author = book_obj.author
        book_finded_obj.category = book_obj.category
        book_finded = book_finded_obj.to_dict()
        datastore.books[book_index] = book_finded
        return book_finded, 200


@ns.route('/delete_book/<string:title>')
@ns.doc(params={'title': 'Book title'})
class BooksDELETEResource(Resource):
    def delete(self, title):
        dumb_book = Book(**{
            'title': title,
            'author': "",
            'category': ""
        })
        _, book_index = _find_book_in_bookstore(dumb_book)
        if book_index >= 0:
            del datastore.books[book_index]
            return 1, 200
        return 0, 200


def _find_book_in_bookstore(book: Book):
    book_finded: Book | None = None
    book_index: int | None = None

    for index, b in enumerate(datastore.books):
        if b['title'].casefold() == book.title.casefold():
            book_finded = b
            book_index = index
            break

    return book_finded, book_index


def _check_required_fields(object, required_fields: list[str]):
    fields_not_found = []
    for field in required_fields:
        if object[field] == None:
            fields_not_found.append(field)
    if fields_not_found:
        raise ValueError('Missing fields : ' + fields_not_found)
