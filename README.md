# front_vanilla

Minimal BookStore frontend with no UI framework — `index.html` + `main.js` ES module.

Intended as a reference implementation: no UI framework, no bundler config, fully spec-compliant.

## Approach

- `index.html` — markup and CSS
- `main.js` — ES module with all CRUD logic (`fetch` calls, DOM rendering)
- No UI framework, no bundler config
- Served with [Vite](https://vite.dev) (dev server with hot reload, zero config for vanilla HTML/JS)
- DOM manipulation via `textContent` (no `innerHTML` with data, to avoid XSS)

## Run

```sh
make install
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
| Makefile | `make install` (`npm install`) + `make dev` |
| Dev environment | `.devcontainer/devcontainer.json` |
