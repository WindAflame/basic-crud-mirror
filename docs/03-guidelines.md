# Guidelines

## API in REST

The backend must expose a RESTful API that:

- Uses standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`)
- Returns appropriate HTTP status codes
- Exchanges data in JSON format
- Strictly follows the routes and contracts defined in [02-resources.md](02-resources.md)

## Doc API = OpenAPI (Swagger or other)

The backend must expose auto-generated API documentation accessible via the `/docs` route, using an OpenAPI-compatible tool (Swagger UI, ReDoc, etc.).

The documentation must reflect all available routes and their request/response schemas.

## Can be deployed with docker

Every service (backend or frontend) must be runnable using:

- A `Makefile` with at minimum `make install` and `make dev` targets
- A `Dockerfile` or a `.devcontainer` configuration

This ensures consistency across development environments and CI pipelines.

## Any API or Front in this project can be connected

All backend implementations must strictly follow the API contract defined in [02-resources.md](02-resources.md), including:

- Route paths and HTTP methods
- Request body shapes
- Response body shapes and status codes
- CORS headers enabled (to allow any frontend to connect)

All frontend implementations must:

- Consume the backend through the documented REST routes
- Display the BookStore interface as described in [02-resources.md](02-resources.md)
- Be configurable to point to any backend URL via an environment variable
