# 🧠 Django Projects

This repository is part of my journey to master **Django** for backend development. Each subproject helps me learn and apply new Django concepts, from user authentication and CRUD to admin management, filtering, and user permissions.

---

## 📚 Projects

### 📰 [Newspaper App](newspaper/)

A basic news publishing app built to practice core Django functionalities including authentication, permissions, CRUD operations, and model relationships.

#### 🔧 Features

- **User Authentication**: Signup, Login, Logout, Change password
- **Article Management**:
  - CRUD operations on articles
  - Only authenticated users can create
  - Only article authors can edit or delete
- **Comments System**:
  - Logged-in users can add comments
  - Comments are filtered for bad words

---

### 📝 [Blog App](blog/)

A more advanced blog platform exploring custom admin features, user promotions, automatic post deletion based on dislikes, category filtering, pagination, and user subscriptions.

#### 🔧 Features

- **User System**: Signup, Login, Logout
- **Admin Panel for Superusers**:
  - Manage posts, categories, and forbidden words
  - Promote users to superusers
- **Posts**:
  - CRUD operations
  - Auto-delete after 10 dislikes
  - Like/dislike system
- **Categories Sidebar**:
  - View and subscribe/unsubscribe to categories
- **Homepage Pagination**:
  - 5 posts per page
  - Latest 5 posts section
- **Comments**:
  - Only for logged-in users
  - Filtered for forbidden words

---

## 🛠️ Tech Stack

- **Backend**: Django
- **Database**: SQLite (default), MySQL
- **Frontend**: Django Templates (HTML + Bootstrap)

---

## 📌 Next Steps

- Add deployment configuration for Heroku or Render
- Add more projects exploring Django REST Framework and APIs
- Implement test coverage for each app

---

## 🤝 Contributions

This is a personal learning repository, but contributions and suggestions are welcome.
