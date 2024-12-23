import { Post, Route, Get, Put, Delete, Controller } from "tsoa";
import BookModel from "../models/book";


@Route("/books")
class BooksController extends Controller {
    @Post("/create_book")
    public async postCreate(): Promise<BookModel> {
        return {} as BookModel;
    }
    @Get("/")
    public async getList(): Promise<BookModel[]> {
        return [];
    }
    @Put("/update_book")
    public async putUpdate(): Promise<BookModel> {
        return {} as BookModel;
    }
    @Delete("/delete_book")
    public async delete(): Promise<number> {
        return 0;
    }
}

export default BooksController;