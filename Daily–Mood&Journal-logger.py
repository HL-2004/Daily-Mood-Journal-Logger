import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3
from datetime import datetime

conn = sqlite3.connect('mood_journal.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS journal
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT, mood TEXT, note TEXT)''')
conn.commit()

def save_entry():
    mood = mood_var.get()
    note = note_entry.get("1.0", tk.END).strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if mood and note:
        c.execute("INSERT INTO journal (date, mood, note) VALUES (?, ?, ?)", (date, mood, note))
        conn.commit()
        messagebox.showinfo("Saved", "Your mood and journal were saved!")
        note_entry.delete("1.0", tk.END)
        show_logs()
    else:
        messagebox.showwarning("Missing", "Please select mood and enter a note.")

def show_logs():
    logs_text.delete("1.0", tk.END)
    c.execute("SELECT * FROM journal ORDER BY id DESC")
    rows = c.fetchall()
    if not rows:
        logs_text.insert(tk.END, "No logs found.\n")
    else:
        for row in rows:
            logs_text.insert(tk.END, f"ID: {row[0]}\nDate: {row[1]}\nMood: {row[2]}\nNote: {row[3]}\n{'-'*30}\n")

def delete_log():
    try:
        delete_id = int(delete_entry.get())
        c.execute("DELETE FROM journal WHERE id = ?", (delete_id,))
        conn.commit()
        if c.rowcount:
            messagebox.showinfo("Deleted", f"Log ID {delete_id} deleted.")
        else:
            messagebox.showwarning("Not Found", f"No log found with ID {delete_id}.")
        delete_entry.delete(0, tk.END)
        show_logs()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid numeric ID.")

def clear_all_logs():
    if messagebox.askyesno("Confirm", "Delete ALL journal entries?"):
        c.execute("DELETE FROM journal")
        conn.commit()
        show_logs()

root = tk.Tk()
root.title("Daily Mood & Journal Logger")
root.geometry("400x600")

tk.Label(root, text="Select Your Mood", font=("Arial", 12, "bold")).pack(pady=5)
mood_var = tk.StringVar()
mood_options = ["Happy", "Sad", "Angry", "Excited", "Tired"]
for mood in mood_options:
    tk.Radiobutton(root, text=mood, variable=mood_var, value=mood).pack(anchor='w')

tk.Label(root, text="Journal Entry:", font=("Arial", 12)).pack(pady=5)
note_entry = tk.Text(root, height=5, width=45)
note_entry.pack()

tk.Button(root, text="Save Entry", command=save_entry, bg="lightgreen").pack(pady=10)

tk.Label(root, text="Journal Logs", font=("Arial", 12, "bold")).pack(pady=5)
logs_text = scrolledtext.ScrolledText(root, width=45, height=12)
logs_text.pack()
show_logs()

tk.Label(root, text="Delete Log by ID:", font=("Arial", 10)).pack(pady=5)
delete_entry = tk.Entry(root, width=10)
delete_entry.pack()
tk.Button(root, text="Delete Log", command=delete_log, bg="salmon").pack(pady=3)

tk.Button(root, text="Clear All Logs", command=clear_all_logs, bg="red", fg="white").pack(pady=10)

root.mainloop()