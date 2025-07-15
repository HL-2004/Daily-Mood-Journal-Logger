
# 📔 Daily Mood & Journal Logger

A personal mood and journal tracking app built with **Python (Tkinter + SQLite3)**, designed for simplicity, mental well-being, and self-reflection.

---

## 🧠 Features

| Feature              | Description                                           |
|----------------------|-------------------------------------------------------|
| 💾 Save Entry         | Record mood and a journal note with date & time      |
| 📜 View Logs          | See all past entries with ID and scrollable display  |
| ❌ Delete by ID        | Delete a specific journal entry using its ID         |
| 🧹 Clear All Logs      | Remove all entries (with confirmation)               |
| 🖱 Scrollable Log View | Smooth scrollable log area for long journals         |

---


## 🛠 Technologies Used

- **Python 3**
- **Tkinter** – GUI creation
- **sqlite3** – Local database to store entries
- **datetime** – For timestamping each mood log
- **ScrolledText** – For smooth log display

---

## 🗂️ File Structure

📁 mood-journal-logger/ ├── mood_logger.py         # Main application file ├── mood_journal.db        # SQLite3 DB file (auto-created) ├── README.md              # Project documentation ├── app_icon.png           # Optional logo (for GUI or web) └── screenshots/           # Optional screenshots for portfolio

---

## ▶️ How to Run

1. **Install Python 3.**  
2. Save the code into a file called `mood_logger.py`.  
3. Open terminal or Pydroid 3 and run:

```bash
python mood_logger.py

No additional libraries are required. This runs on any standard Python installation or Pydroid 3.


---

💾 Database Format

Column	Type	Description

id	INTEGER	Auto-increment log ID
date	TEXT	Timestamp (YYYY-MM-DD HH:MM:SS)
mood	TEXT	Selected mood
note	TEXT	Journal text entry



---

📝 Sample Log Output

ID: 12
Date: 2025-07-15 10:12:30
Mood: Happy
Note: Enjoyed a productive day learning Python!
------------------------------


---

📌 Future Improvements

Add emoji or icons for moods

Export logs as .txt or .csv

Search/filter logs by date or mood

Password protection

Dark mode UI
