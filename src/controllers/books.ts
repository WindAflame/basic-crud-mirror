import BookModel from "../models/book";

export default class BooksController {
    public async postCreate(): Promise<BookModel> {
        return {} as BookModel;
    }
    public async getList(): Promise<BookModel[]> {
        return [];
    }
    public async putUpdate(): Promise<BookModel> {
        return {} as BookModel;
    }
    public async delete(): Promise<number> {
        return 0;
    }
}