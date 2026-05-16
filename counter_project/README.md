# Django Counter Application

A dynamic web application built with Django that tracks and manages user session data. This project demonstrates how to persist information (like a visit counter) across multiple browser requests using Django's built-in session engine.

## 🎯 Project Objectives
* Implementing **Session** management to store client-specific data.
* Initializing, checking, and modifying session keys (`request.session`).
* Handling logic for incrementing counters and clearing session data.
* Using **Redirects** to maintain a clean state after POST actions.
* Creating a responsive UI with custom CSS.

## 🛠️ Tech Stack
* **Framework:** Django
* **Language:** Python 3.x
* **Frontend:** HTML5, Custom CSS

## 📑 Features & Functionality
* **Automatic Counter:** Increments by 1 every time the root route (`/`) is visited or refreshed.
* **Session Reset:** A "Destroy Session" feature that clears all session data and resets the counter to zero.
* **Ninja Bonus (+2):** A dedicated button and route to increment the counter by 2.
* **Sensei Bonus (Specific Amount):** A form that allows users to input a custom integer to increment the counter by that specific value.
* **Modern UI:** A centered "Card" layout with a large, clear display for the current count.

## 🚀 Installation & Setup
1. Clone this repository.
2. Navigate to the project folder:
   ```bash
   cd counter_project