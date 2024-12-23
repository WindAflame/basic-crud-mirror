import express from "express";
import BooksController from "../controllers/books";

const router = express.Router();

/**
  * @swagger
  * /books/create_book:
  *   post:
  *     summary: Create Book
  *     responses:
  *       200:
  *         description: Returns an object with uptime, date and message
  */
router.post("/create_book", async (_req, res) => {
  const controller = new BooksController();
  const response = await controller.postCreate();
  return res.send(response);
});

/**
  * @swagger
  * /books/:
  *   get:
  *     summary: Read All Books
  *     responses:
  *       200:
  *         description: Successful Response
  *         content:
  *           application/json:
  *             schema:
  *               $ref: '#/components/schemas/Book'
  *         
  */
router.get("/", async (_req, res) => {
  const controller = new BooksController();
  const response = await controller.getList();
  return res.send(response);
});

router.put("/update_book", async (_req, res) => {
  const controller = new BooksController();
  const response = await controller.putUpdate();
  return res.send(response);
});

router.delete("/delete_book", async (_req, res) => {
  const controller = new BooksController();
  const response = await controller.delete();
  return res.send(response);
});

export default router;