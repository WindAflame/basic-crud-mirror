from flask_restx import fields

book_fields = {
    'title': fields.String(description="Title of the book"),
    'author': fields.String(description="Author of the book"),
    'category': fields.String(description="Category of the book")
}


class Book():
    title = fields.String(description="Title of the book")
    author = fields.String(description="Author of the book")
    category = fields.String(description="Category of the book")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {key: getattr(self, key) for key in book_fields}


# class Book():
#     title = fields.String(description="Title of the book")
#     author = fields.String(description="Author of the book")
#     category = fields.String(description="Category of the book")