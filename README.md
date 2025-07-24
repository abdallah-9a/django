# Django Projects

This repository is part of my journey to master **Django** for backend development.

### [Newspaper](newspaper/)

built to practice core Django functionalities including authentication, permissions, CRUD operations, and model relationships.

---

## Features

- **User Authentication**:

  - Signup, Login, Logout
  - Change password functionality

- **Article Management**:

  - Create, Read, Update, and Delete (CRUD) operations
  - Only authenticated users can create articles
  - Only the **author** of an article can edit or delete it

- **Comments System**:
  - Logged-in users can add comments on articles
  - Comments are automatically **filtered** for bad words

---

## 🛠️ Tech Stack

- **Backend**: Django
- **Database**: SQLite (default)
- **Frontend**: Django Templates (HTML + Bootstrap for styling)
