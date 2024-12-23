# Book Store

## Models

### Book

|Name|Type|
|---|---|
|title|string|
|author|string|
|category|string|

## REST Api

|Method|Route|Response|Description|
|---|---|---|---|
|POST|/books/create_book|Book|To create a Book|
|GET|/books|List[Book]|To get all the values from the Book list|
|PUT|/books/update_book|Book (success) or None (failure)|To update an entry in the book list|
|DELETE|/books/delete_book/:book_title|1 (success) or 0 (failure)|To delete a book in the book list|
|GET|/docs|Swagger UI|Documentation about all routes on the API.|