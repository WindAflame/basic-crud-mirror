import express, { Application } from "express";
import swaggerUi from "swagger-ui-express";
import { RegisterRoutes } from "../build/routes";
import config from "./config";

const app: Application = express();

app.use(express.json());
app.use(express.static("public"));
app.use(
  "/docs",
  swaggerUi.serve,
  swaggerUi.setup(undefined, {
    swaggerOptions: {
      url: "/swagger.json",
    },
  })
);
// Doesn't use this
// app.use(RegisterRoutes);
// Use this
RegisterRoutes(app);

app.listen(config.port, () => {
  console.log("Server is running on port", config.port);
});