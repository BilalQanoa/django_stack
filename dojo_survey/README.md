# Dojo Survey Application

A Django web application designed to collect user feedback through a comprehensive HTML form and display the submitted data on a dynamic results page. This project focuses on handling POST requests and mastering form input types.

## 🎯 Project Objectives
* Building a Django server and application from scratch.
* Implementing HTML forms with various input types (Text, Select, Radio, Checkbox, Textarea).
* Handling **POST** requests and extracting data using `request.POST`.
* Rendering templates with dynamic context data.
* Integrating custom CSS for an enhanced user experience.

## 🛠️ Tech Stack
* **Framework:** Django
* **Language:** Python 3.x
* **Frontend:** HTML5, CSS3 (Custom styling for a professional UI)

## 📑 Features & Functionality
* **Root Route (`/`):** Displays a clean, centered survey form with validation.
* **Result Route (`/result`):** Processes the form data and renders a summary page.
* **Input Variety:** Includes text fields, dropdowns for Dojo locations and languages, and a comments section.
* **Ninja & Sensei Bonuses:** * 🔘 **Radio Buttons:** Added for Gender selection.
    * ☑️ **Checkboxes:** Implemented for Terms and Conditions agreement.
    * 🎨 **Advanced Styling:** Customized CSS to ensure labels and inputs (especially Radio/Checkboxes) are perfectly aligned.

## 🚀 Installation & Setup
1. Clone this repository.
2. Navigate to the project directory.
3. Run the server:
   ```bash
   python manage.py runserver
