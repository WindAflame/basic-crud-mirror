import express from "express";
import swaggerUi from "swagger-ui-express";
import swaggerJSDoc from "swagger-jsdoc";
import config from "../config";

const router = express.Router();


console.log(`Swagger : ${config.port}`);
const swaggerOptions = {
    swaggerDefinition: {
        openapi: '3.0.0',
        info: {
            title: 'Book Store',
            version: "0.1.0",
            description: 'Book Store API Information',
        },
        servers: [
            {
                url: `http://localhost:${config.port}/`
            }
        ],
        components: {
            securitySchemes: {
                bearerAuth: {
                    type: 'http',
                    scheme: 'bearer',
                    bearerFormat: 'JWT',
                },
            }, 
        },
    },
    apis: ['./src/routes/*.ts', './src/models/*.ts']
};
const swaggerDocs = swaggerJSDoc(swaggerOptions);

router.use("/",
    swaggerUi.serve,
    swaggerUi.setup(swaggerDocs)
);

export default router;