import express from "express";
import HealthController from "../controllers/health";
import BookRouter from "./books";
import SwaggerDocs from "./docs";

const router = express.Router();

/**
  * @swagger
  * /health:
  *   get:
  *     summary: Get UpTime of server
  *     responses:
  *       200:
  *         description: Returns an object with uptime, date and message
  */
router.get("/health", async (_req, res) => {
  const controller = new HealthController();
  const response = await controller.getMessage();
  return res.send(response);
});

router.use("/books", BookRouter);
router.use("/docs", SwaggerDocs);
export default router;