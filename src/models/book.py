from flask_restx import fields

book_fields = {
    'id': fields.Integer(description="Identifier of the book", required=False),
    'title': fields.String(description="Title of the book", required=True),
    'author': fields.String(description="Author of the book", required=True),
    'category': fields.String(description="Category of the book", required=True)
}

class Book():

    id: int | None
    title: str
    author: str
    category: str

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {key: getattr(self, key) for key in book_fields}