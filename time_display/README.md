# Django Time Display Project

A sleek, simple Django web application that captures the current server date and time and displays it on a styled web page. This project focuses on data passing from views to templates and integrating static files.

## 🎯 Project Objectives
* Establishing a new Django project and application structure.
* Passing dynamic server-side data (Python `time` module) to the front-end.
* Linking and utilizing static files (CSS) to create a custom user interface.
* Handling root routes and app-specific URL configurations.

## 🛠️ Tech Stack
* **Framework:** Django
* **Language:** Python 3.x
* **Styling:** Custom CSS (Static Files)
* **Time Library:** `time.strftime` (and `datetime` as a Ninja Bonus)

## 📑 Features
* **Live Time Fetching:** Automatically retrieves the current UTC/Local time upon page load.
* **Formatted Display:** Uses Python's `strftime` to format date and time into a readable string (e.g., May 16, 2026 04:30 PM).
* **Responsive Design:** A custom-styled box layout that centers the time display for a modern look.
* **Dual Routing:** Accessible via both the root URL (`/`) and the specific app route (`/time_display`).

## 🥷 Ninja Bonus Task
* Implemented an alternative way to retrieve time data (using the `datetime` module) to practice Python's versatility in handling temporal data.

## 🚀 Installation & Setup
1. Clone this repository to your local machine.
2. Navigate to the project directory:
   ```bash
   cd time_display_project
