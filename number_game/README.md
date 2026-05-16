# Great Number Game 🎯

An interactive web-based guessing game built with Django. The server thinks of a random number between 1 and 100, and the player has 5 attempts to guess it correctly!

## 🎯 Project Objectives
* **Session Management:** Using `request.session` to persist the target number and attempt count across multiple requests.
* **Conditional Rendering:** Dynamically displaying different UI components (Success/Danger boxes) based on the game state.
* **Form Processing:** Handling user input via POST requests and implementing server-side logic for comparisons.
* **State Control:** Implementing a "Reset" functionality to clear sessions and restart the game.

## 🛠️ Tech Stack
* **Framework:** Django 3.x/4.x
* **Language:** Python 3.x
* **Styling:** Custom CSS (focused on the "Wireframe" look with large colored boxes).

## 📑 Game Features & Logic
* **Random Generation:** Uses Python's `random` module to pick a secret number on the first visit.
* **Feedback Loops:** * 🔴 **Too Low:** Displayed in a red box if the guess is below the target.
    * 🔴 **Too High:** Displayed in a red box if the guess is above the target.
    * 🟢 **Correct:** Displayed in a green box when the player wins.
* **Sensei Bonus (Limited Attempts):** Players are limited to **5 attempts**. If they fail, a "You Lose" message appears with the correct number.
* **Dynamic UI:** The input form automatically disappears once the game is over (Win or Loss) to prevent further guesses.

## 🚀 Installation & Setup
1. Clone the repository.
2. Navigate to the project folder.
3. Run migrations (to initialize Django's session table):
   ```bash
   python manage.py migrate