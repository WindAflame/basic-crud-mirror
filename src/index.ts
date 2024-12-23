import express, { Application } from "express";
import Router from "./routes";
import config from "./config";

const app: Application = express();
 
app.use(express.json());
app.use(express.static("public"));
app.use(Router);

app.listen(config.port, () => {
  console.log("Server is running on port", config.port);
});