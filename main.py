import tkinter as tk
from tkinter import ttk
from datetime import datetime
import matplotlib.pyplot as plt
import json

# Function to save journal entries to JSON file
def save_entry():
    entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mood = mood_var.get()
    thoughts = thoughts_text.get("1.0", "end-1c")

    # Read existing data from JSON file
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Add the new entry to the data
    data.append({
        "Date": entry_date,
        "Mood": mood,
        "Thoughts": thoughts
    })

    # Write the updated data back to the JSON file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    clear_fields()

# Function to clear input fields
def clear_fields():
    mood_var.set("")
    thoughts_text.delete("1.0", "end")

# Create the main application window
app = tk.Tk()
app.title("Mental Health Journal")

# Create and configure widgets
mood_label = tk.Label(app, text="Mood:")
mood_var = tk.StringVar()
mood_entry = ttk.Combobox(app, textvariable=mood_var, values=["Happy", "Sad", "Anxious", "Neutral", "Other"])

thoughts_label = tk.Label(app, text="Thoughts/Feelings:")
thoughts_text = tk.Text(app, height=10, width=30)

save_button = tk.Button(app, text="Save Entry", command=save_entry)
clear_button = tk.Button(app, text="Clear Fields", command=clear_fields)

# Create a mood analytics graph (you can use libraries like Matplotlib for this)
# You'll need to install Matplotlib: pip install matplotlib

def show_mood_analytics():
    # Retrieve mood data from the journal (you may need to parse the journal file)
    # For simplicity, let's assume a static mood dataset
    moods = ["Happy", "Sad", "Neutral", "Anxious"]
    mood_counts = [12, 5, 8, 3]

    # Create a bar chart
    plt.bar(moods, mood_counts)
    plt.xlabel("Mood")
    plt.ylabel("Count")
    plt.title("Mood Analytics")
    plt.show()

show_analytics_button = tk.Button(app, text="Show Mood Analytics", command=show_mood_analytics)

# Progress Tracking
goal_label = tk.Label(app, text="Self-Improvement Goal:")
goal_entry = tk.Entry(app)
goal_progress = tk.Label(app, text="Progress: 0%")

update_progress_button = tk.Button(app, text="Update Progress", command = goal_progress)

def update_progress():
    # You can calculate progress here based on user input and update goal_progress
    # For example, if you have a numeric goal, you can use goal_entry.get() to retrieve the goal value.
    # Update the progress label accordingly.
    # You might need to use some data storage to save goals and progress.

# Feedback
    feedback_window = None

def open_feedback_form():
    global feedback_window
    feedback_window = tk.Toplevel(app)
    feedback_window.title("Feedback Form")

    feedback_label = tk.Label(feedback_window, text="Please provide your feedback:")
    feedback_text = tk.Text(feedback_window, height=10, width=30)
    submit_feedback_button = tk.Button(feedback_window, text="Submit Feedback", command=submit_feedback)

    feedback_label.pack()
    feedback_text.pack()
    submit_feedback_button.pack()

def submit_feedback():
    feedback = feedback_text.get("1.0", "end-1c")
    # You can save the feedback to a file or database, or send it to your server for analysis.

feedback_button = tk.Button(app, text="Provide Feedback", command=open_feedback_form)

# Grid layout for widgets
mood_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
mood_entry.grid(row=0, column=1, padx=10, pady=5)
thoughts_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
thoughts_text.grid(row=1, column=1, padx=10, pady=5, rowspan=3)

# Place both buttons in the same row, with the Clear button in column 2
save_button.grid(row=4, column=0, padx=10, pady=10)
clear_button.grid(row=4, column=1, padx=10, pady=10)
show_analytics_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Progress Tracking and Feedback
goal_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
goal_entry.grid(row=6, column=1, padx=10, pady=5)
goal_progress.grid(row=7, column=0, padx=10, pady=5, columnspan=2)
update_progress_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
feedback_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter main loop
app.mainloop()
# this is new