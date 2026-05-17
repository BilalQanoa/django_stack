# 🥷 Ninja Gold Game (Django Edition)

An interactive mini-game built using the **Django Framework**. The player takes on the role of a ninja visiting various locations to accumulate gold, with each location offering different levels of reward and risk.

---

## 🕹️ Game Mechanics

| Location   | Reward/Risk     | Description                                  |
| :--------- | :-------------- | :------------------------------------------- |
| **Farm**   | +10 to 20 gold  | Stable and safe income.                      |
| **Cave**   | +5 to 10 gold   | Decent rewards with minimal effort.          |
| **House**  | +2 to 5 gold    | Low reward, but very consistent.             |
| **Casino** | -50 to +50 gold | High risk, high reward. Can take your money! |

---

## 🛠️ Technical Features

* **Django Sessions:** Managed player's total gold and activity history across requests.
* **POST Routing:** Securely handled game actions via `/process_money`.
* **Activity Logger:** A dynamic log that tracks every move with timestamps and color-coded feedback (Green for wins, Red for losses).
* **Static File Management:** Custom CSS integrated within the app's structure for a unique "Ninja" look and feel.
* **Bootstrap Integration:** Responsive UI using Bootstrap 4.5.

---

## 📂 Project Structure

```text
ninja_gold_project/
├── ninja_app/              # Main application folder
│   ├── static/             # Static files (CSS)
│   │   └── css/
│   │       └── style.css
│   ├── templates/          # HTML Templates
│   │   └── index.html
│   ├── views.py            # Game logic (money calculation & sessions)
│   └── urls.py             # App-specific routing
├── manage.py
└── README.md