# Contributing

## How to contribute

Fork this repository and create a branch following the naming convention below. Once your implementation is ready, open a pull request and add your entry to [propositions/index.md](propositions/index.md).

## Branch naming

```text
propositions/<github-username>/<type>_<framework>
```

- `<type>` is either `back` or `front`
- `<framework>` is the name of the framework used (e.g. `fastapi`, `nestjs`, `react`, `vue`)

Examples:

- `propositions/johndoe/back_fastapi`
- `propositions/johndoe/front_react`

## Requirements

Regardless of the language or framework chosen, every contribution must satisfy the guidelines defined in [docs/03-guidelines.md](docs/03-guidelines.md).

### All services (backend and frontend)

- Must include a `Makefile` with at minimum `make install` and `make dev`
- Must include a `Dockerfile` or a `.devcontainer` configuration

### Backend

- Must expose a REST API following the contract in [docs/02-resources.md](docs/02-resources.md)
- Must expose API documentation at `/docs` (OpenAPI / Swagger)
- Must enable CORS to allow any frontend to connect

### Frontend

- Must consume the backend via the REST routes defined in [docs/02-resources.md](docs/02-resources.md)
- Must implement all four BookStore views (list, create, edit, delete)
- Must accept the backend URL via an environment variable

## Register your proposition

Add a row to the table in [propositions/index.md](propositions/index.md):

```markdown
| YourGithubName | propositions/YourGithubName/back_yourframework | Language | [Framework](https://framework-url) | [View on GitHub](https://github.com/your-username/your-repo/tree/your-branch) |
```
