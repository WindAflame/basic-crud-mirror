from flask_restx import Namespace

from .book import book_fields

ns = Namespace('models')

book_model = ns.model('Book', book_fields)
