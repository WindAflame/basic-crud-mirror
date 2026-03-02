// ---------------------------------------------------------------------------
// Configuration
// ---------------------------------------------------------------------------

// To point to a different backend, run in the browser console:
//   localStorage.setItem('API_URL', 'http://your-host:8000')
const API = localStorage.getItem('API_URL') || 'http://localhost:8000';

// ---------------------------------------------------------------------------
// State
// ---------------------------------------------------------------------------

let books = [];
let editingTitle = null;

// ---------------------------------------------------------------------------
// Render
// ---------------------------------------------------------------------------

function render() {
  const tbody = document.getElementById('tbody');
  tbody.replaceChildren(
    ...books.map((book, i) => {
      const tr = document.createElement('tr');

      // Data cells — use textContent to avoid XSS
      ['title', 'author', 'category'].forEach(key => {
        const td = document.createElement('td');
        td.textContent = book[key];
        tr.appendChild(td);
      });

      // Action buttons
      const td = document.createElement('td');

      const editBtn = document.createElement('button');
      editBtn.textContent = 'Edit';
      editBtn.className = 'btn-edit';
      editBtn.onclick = () => startEdit(i);

      const delBtn = document.createElement('button');
      delBtn.textContent = 'Delete';
      delBtn.className = 'btn-delete';
      delBtn.onclick = () => deleteBook(book.title);

      td.append(editBtn, delBtn);
      tr.appendChild(td);
      return tr;
    })
  );
}

// ---------------------------------------------------------------------------
// Load all books  —  GET /books
// ---------------------------------------------------------------------------

async function loadBooks() {
  const res = await fetch(`${API}/books`);
  books = await res.json();
  render();
}

// ---------------------------------------------------------------------------
// Create / Update  —  POST /books/create_book  |  PUT /books/update_book
// ---------------------------------------------------------------------------

document.getElementById('form').addEventListener('submit', async e => {
  e.preventDefault();
  const book = {
    title:    document.getElementById('title').value,
    author:   document.getElementById('author').value,
    category: document.getElementById('category').value,
  };

  if (editingTitle) {
    await fetch(`${API}/books/update_book`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(book),
    });
    stopEdit();
  } else {
    await fetch(`${API}/books/create_book`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(book),
    });
    e.target.reset();
  }
  loadBooks();
});

// ---------------------------------------------------------------------------
// Edit helpers
// ---------------------------------------------------------------------------

function startEdit(i) {
  const book = books[i];
  editingTitle = book.title;
  document.getElementById('title').value    = book.title;
  document.getElementById('author').value   = book.author;
  document.getElementById('category').value = book.category;
  document.getElementById('submit-btn').textContent = 'Update';
  document.getElementById('cancel-btn').hidden = false;
}

function stopEdit() {
  editingTitle = null;
  document.getElementById('form').reset();
  document.getElementById('submit-btn').textContent = 'Add';
  document.getElementById('cancel-btn').hidden = true;
}

document.getElementById('cancel-btn').addEventListener('click', stopEdit);

// ---------------------------------------------------------------------------
// Delete  —  DELETE /books/delete_book/:book_title
// ---------------------------------------------------------------------------

async function deleteBook(title) {
  if (!confirm(`Delete "${title}"?`)) return;
  await fetch(`${API}/books/delete_book/${encodeURIComponent(title)}`, {
    method: 'DELETE',
  });
  loadBooks();
}

// ---------------------------------------------------------------------------
// Init
// ---------------------------------------------------------------------------

loadBooks();
