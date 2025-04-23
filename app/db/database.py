import json
import os

from pydantic import TypeAdapter

from ..models.book import Book

BOOKS_JSON_PATH = "resources/books.json"
BOOKS: list[Book] = []


def initialise():
    BOOKS.extend(
        TypeAdapter(list[Book]).validate_python(
            __load_from_json_file(BOOKS_JSON_PATH)
        )
    )


def __load_from_json_file(path: str) -> any:
    if not os.path.isfile(path):
        raise FileNotFoundError("File path not found : " + path)
    return json.load(open(path))
