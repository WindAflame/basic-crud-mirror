# front_vanilla

Minimal BookStore frontend with no dependencies — a single HTML file.

Intended as a reference implementation: no framework, no build step, fully spec-compliant.

## Approach

- Single file `index.html` — all HTML, CSS, and JavaScript
- No framework, no dependencies, no build step
- Served with [Vite](https://vite.dev) (hot reload, no config needed for vanilla HTML/JS)
- DOM manipulation (no innerHTML with data, to avoid XSS)

## Run

```sh
make dev
```

App available at `http://localhost:5173`

## Configure the backend URL

By default the frontend connects to `http://localhost:8000`. To point to a different backend, run this once in the browser console:

```js
localStorage.setItem('API_URL', 'http://your-backend:8000')
```

## Spec compliance

| Requirement | How |
|---|---|
| Consume REST API | `fetch()` calls to all four routes |
| Book list view | Table rendered on load |
| Create book | Form submits `POST /books/create_book` |
| Edit book | Form pre-filled, submits `PUT /books/update_book` |
| Delete book | Button calls `DELETE /books/delete_book/:title` |
| Configurable backend URL | `localStorage` override |
| Makefile | `make install` (no-op) + `make dev` |
| Dev environment | `.devcontainer/devcontainer.json` |
