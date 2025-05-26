from http import HTTPStatus
import json

from flask import request
from flask_restx import Namespace, Resource

from dao.book_dao import BookDAO
import datastore as DS
from models.api_models import book_model, book_parser
from models.book import Book

ns = Namespace('books', description='Manage a bookstore')
dao = BookDAO()

@ns.route('/', endpoint='')
class BooksGETResource(Resource):

    @ns.response(HTTPStatus.OK.value, "Get the book list")
    @ns.marshal_list_with(book_model)
    def get(self):
        """
        Returns Books from database
        """
        return dao.read_all(), 200


@ns.route('/create_book', endpoint='create_book')
class BooksPOSTResource(Resource):
    
    @ns.response(HTTPStatus.OK.value, "Object added")
    @ns.expect(book_parser)
    def post(self):
        """
        Create a book
        """
        args = book_parser.parse_args()
        book = Book(**args)
        book.id = len(DS.books)
        return dao.create(book).to_dict(), 200


@ns.route('/update_book', endpoint='update_book')
class BooksPUTResource(Resource):
    @ns.expect(book_model)
    def put(self):
        book = Book(**book_model)
        return dao.update(book['id'], Book(**book)).to_dict(), 200


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
        return dao.delete(book_index), 200


def _find_book_in_bookstore(book: Book):
    book_finded: Book | None = None
    book_index: int | None = None

    for index, b in enumerate(DS.books):
        if b['title'].casefold() == book.title.casefold():
            book_finded = b
            book_index = index
            break

    return book_finded, book_index
