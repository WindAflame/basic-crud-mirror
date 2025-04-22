# basic-crud

The aim of this project is to define an ultra-minimalist use case to try out the development of several languages or frameworks to achieve the same objective.

The specifications are drawn from my personal experience and are intended to reproduce the development environment contexts I have mostly worked in.

More details in the project documentation, [here](docs/index.md)

## Summary

* The project must have a backend and a fontend, in order to perform a CRUD.
* The database is supplied as a [flat file in JSON format](resources/books.json). (This is a personal choice to simplify development. I recommend that you use a library that lets you manipulate a real database like PostgreSQL or MongoDB with this database initialization file.)
* API documentation with swagger is required.
* All projects, backend or frontend, must be installed and run with a Makefile, to unify CI and development workstation behavior.
* All projects, backend or frontend, must be able to run in .devcontainer or docker, in order to unify the development and deployment environment. (Accessory, to be able to launch the project from Github).

## Backend

|Branch|Language|Framework|
|---|---|---|
|[api_express_swagger_jsdoc](https://github.com/WindAflame/basic-crud/tree/api_express_swagger_jsdoc)|Typescript|[Express.js](https://expressjs.com/)|
|[api_express_swagger_tsoa](https://github.com/WindAflame/basic-crud/tree/api_express_swagger_tsoa)|Typescript|[Express.js](https://expressjs.com/)|
|[api_fastapi](https://github.com/WindAflame/basic-crud/tree/api_fastapi)|Python|[FastAPI](https://fastapi.tiangolo.com/)|
|[api_flask](https://github.com/WindAflame/basic-crud/tree/api_flask)|Python|[Flask](https://flask.palletsprojects.com/)|
|[api_nestjs_swagger](https://github.com/WindAflame/basic-crud/tree/api_nestjs_swagger)|Typescript|[Nestjs](https://nestjs.com/)|

## Frontend

In progress
