# back_fastapi_minimal

Minimal BookStore REST API implemented with FastAPI.

Intended as a reference implementation: single file, fully spec-compliant.

## Approach

- Single file `main.py` — the entire API
- FastAPI provides built-in OpenAPI/Swagger at `/docs`
- CORS enabled for all origins (one middleware line)
- Flat JSON file as database (`books.json`)
- `uv` for dependency management (no manual venv)

## Run

```sh
make install
make dev
```

- API: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`

## Spec compliance

| Requirement | How |
|---|---|
| REST API | FastAPI routes with correct HTTP methods and status codes |
| OpenAPI / Swagger | Built-in at `/docs` |
| CORS | `CORSMiddleware` with `allow_origins=["*"]` |
| Makefile | `make install` + `make dev` |
| Dev environment | `.devcontainer/devcontainer.json` |
