from datetime import datetime

from flask import Flask
from flask_restx import Api

import datastore as DS
from dao.book_dao import BookDAO
from models.api_models import ns as ressources_models_namespace
from models.book import Book
from resources.book import ns as ressources_book_namespace
from resources.health import ns as ressources_health_namespace
from settings import BOOKS_JSON_PATH
from utils import Utils

# ============================================
# Methods
# ============================================

def init_books():
    try: 
        data: list[Book] = Utils.load_from_json_file(BOOKS_JSON_PATH)
        for book in data:
            book_instance = Book(**book)
            BookDAO().create(book_instance)
        print("Books loaded from JSON")
    except Exception as e:
        print(f"Error loading books from JSON: {e}")

# ============================================
# Main
# ============================================
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(
    app,
    title="Minimal REST API",
    description="A mini REST API with Flask and Flask_RESTx",
    version="0.1.0",
    doc="/docs/"
)
# Register start time
DS.start_time = datetime.now()
init_books()


# ============================================
# Add Resource - With RESTx
# ============================================
api.add_namespace(ressources_models_namespace)
api.add_namespace(ressources_health_namespace)
api.add_namespace(ressources_book_namespace)
