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

- **User System**:
  - Signup with email validation, Login, Logout
  - Custom user creation form with email requirement
- **Admin Panel for Superusers**:
  - Comprehensive management dashboard
  - Manage posts, categories, and forbidden words
  - Promote users to superusers
  - User management with promotion capabilities
- **Posts**:
  - CRUD operations with tagging system
  - Auto-delete after 10 dislikes
  - Like/dislike system with toggle functionality
  - Similar posts recommendation based on tags
  - Tag-based post filtering and browsing
- **Categories System**:
  - Category-based post organization
  - Subscribe/unsubscribe to categories with email notifications
  - Category details pages with filtered posts
- **Email Notifications**:
  - Subscription confirmation emails (HTML & plain text)
  - SMTP email backend integration
  - Graceful email error handling
- **Homepage Features**:
  - Pagination (5 posts per page)
  - Latest posts display
  - Category sidebar with subscription status
- **Comments System**:
  - Only for logged-in users
  - Real-time forbidden word filtering with censorship
  - Comments linked to specific posts
- **Tagging System**:
  - Django-taggit integration for post tagging
  - Tag-based post discovery and filtering
- **Database**:
  - MySQL integration with custom configuration
  - Egypt timezone support

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
