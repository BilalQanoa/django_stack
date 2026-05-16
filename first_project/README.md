# First Django Project: Routing & Views

This is my first Django project where I practiced the core concepts of **URL Routing**, **View Methods**, and **Route Parameters**. The project demonstrates how Django handles different types of responses including strings, redirects, and JSON data.

## 🎯 Objectives
* Setting up a Django project and app from scratch.
* Mastering Django's URL routing system.
* Handling dynamic URL parameters.
* Understanding different response types (`HttpResponse`, `redirect`, `JsonResponse`).

## 🛠️ Features & Routes

The application includes the following routes and functionalities:

| Route | Method | Description |
| :--- | :--- | :--- |
| `/` | `root` | Redirects to the `/blogs` route. |
| `/blogs` | `index` | Displays a placeholder for the list of all blogs. |
| `/blogs/new` | `new` | Displays a placeholder for a new blog creation form. |
| `/blogs/create` | `create` | Processes the creation and redirects back to `/`. |
| `/blogs/<number>` | `show` | Displays the blog number dynamically (e.g., Blog #15). |
| `/blogs/<number>/edit` | `edit` | Displays a placeholder to edit a specific blog. |
| `/blogs/<number>/delete` | `destroy` | Redirects to `/blogs` after "deleting" a blog. |
| `/blogs/json` | `json_data` | **Bonus:** Returns a JSON response with title and content. |

## 🚀 How to Run the Project
1. Clone the repository.
2. Navigate to the project folder.
3. Run the server:
   ```bash
   python manage.py runserver
