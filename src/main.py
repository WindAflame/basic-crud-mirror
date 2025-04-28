import time

from flask import Flask
from flask_restx import Api

import datastore
from models.api_models import ns as ressources_models_namespace
from resources.health import ns as ressources_health_namespace
from resources.book import ns as ressources_book_namespace

# ============================================
# Main
# ============================================
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(
    app,
    title="Flask API",
    version="0.1.0",
    doc="/docs/"
)
# Register start time
datastore.start_time = time.time()


# ============================================
# Add Resource
# ============================================
# With RESTful
# api.add_resource(HealthGETResource, '/health')
# api.add_resource(BooksGETResource, '/books/')
# api.add_resource(BooksPOSTResource, '/books/create_book/')
# api.add_resource(BooksPUTResource, '/books/update_book/')
# api.add_resource(BooksDELETEResource, '/books/delete_book/')

# With RESTx
api.add_namespace(ressources_models_namespace)
api.add_namespace(ressources_health_namespace)
api.add_namespace(ressources_book_namespace)