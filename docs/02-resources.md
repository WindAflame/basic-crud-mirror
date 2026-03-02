# Resources

## Data models

### Book

|Name|Type|
|---|---|
|title|string|
|author|string|
|category|string|

## REST Api

|Method|Route|Status|Response|Description|
|---|---|---|---|---|
|POST|/books/create_book|201|Book|To create a Book|
|GET|/books|200|List[Book]|To get all the values from the Book list|
|PUT|/books/update_book|200 / 404|Book / None|To update an entry in the book list|
|DELETE|/books/delete_book/:book_title|200 / 404|1 / 0|To delete a book in the book list|
|GET|/docs|200|Swagger UI|Documentation about all routes on the API.|

## Frontend interfaces

The frontend must implement the following views:

|View|Description|
|---|---|
|Book list|Display all books fetched from `GET /books`|
|Create book|Form to submit a new book via `POST /books/create_book`|
|Edit book|Form to update an existing book via `PUT /books/update_book`|
|Delete book|Action to remove a book via `DELETE /books/delete_book/:book_title`|