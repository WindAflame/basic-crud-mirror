from flask_restx import Namespace

from .book import book_fields

ns = Namespace('models')

book_model = ns.model('Book', book_fields)
book_parser = ns.parser()
book_parser.add_argument("title", type=str, location="form")
book_parser.add_argument("author", type=str, location="form")
book_parser.add_argument("category", type=str, location="form")
