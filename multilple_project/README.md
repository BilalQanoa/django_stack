# 🏢 Django Multiple Apps Project

A modular Django project designed to demonstrate the power of **App Reusability**. This project integrates three independent modules (Blogs, Surveys, and Users) into a single unified system using clean routing and namespaces.

---

## 🏗️ Project Structure
The project is divided into three main apps, each handling a specific domain:

1.  **Blogs App:** Manages blog listings, creation, editing, and deletion.
2.  **Surveys App:** Handles survey displays and creation forms.
3.  **Users App:** Manages user registration, login, and profile listings.

---

## 🔗 Routing Architecture

### 1. Blogs Module (`/blogs`)
* `GET /blogs` - Display all blogs (Index).
* `GET /blogs/new` - Form to create a new blog.
* `POST /blogs/create` - Process new blog and redirect to index.
* `GET /blogs/<id>` - Display a specific blog by its ID.
* `GET /blogs/<id>/edit` - Edit a specific blog.
* `POST /blogs/<id>/delete` - Remove a blog and redirect.

### 2. Surveys Module (`/surveys`)
* `GET /surveys` - List all surveys.
* `GET /surveys/new` - Form to add a new survey.

### 3. Users Module (Root)
* `GET /register` - User registration page.
* `GET /login` - User login page.
* `GET /users/new` - Shortcut to registration.
* `GET /users` - List all registered users.

---

## 🥷 Ninja Features (Bonuses)
* **Smart Root Redirection:** The root URL (`/`) is dynamically linked to the `Blogs` app.
* **Namespace Usage:** Implemented `app_name` in `urls.py` to allow clean redirects using `redirect('blogs:index')`.
* **DRY Principle:** Reused the registration logic for multiple routes to ensure code maintainability.

---

## 🛠️ Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-link>
    cd django_multiple_apps
    ```

2.  **Install Django:**
    ```bash
    pip install django
    ```

3.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Start the Server:**
    ```bash
    python manage.py runserver
    ```

5.  **Explore the Project:**
    Navigate to `http://localhost:8000/` to see the automatic redirection to Blogs.

---

## 🧩 Learning Objectives Achieved
- [x] Creating and registering multiple Django apps.
- [x] Using `include()` for distributed URL routing.
- [x] Handling dynamic URL parameters (`<int:number>`).
- [x] Mastering `Redirect` between different apps.
- [x] Implementing Namespacing for robust link management.

---
**Built as part of the Full Stack Django Development Path.**