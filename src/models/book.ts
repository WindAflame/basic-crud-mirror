/**
  * @swagger
  * components:
  *   schemas:
  *     Book:
  *       type: object
  *       properties:
  *         title:
  *           type: string
  *           description: a title
  *         author:
  *           type: string
  *           description: an author
  *         category:
  *           type: string
  *           description: a category 
  */
export default interface BookModel {
    title: string;
    author: string;
    category: string;
}