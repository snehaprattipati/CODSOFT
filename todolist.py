import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def add_task():
    task = entry.get().strip()  # Strip leading/trailing whitespace
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        if index:
            listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    except:
        messagebox.showwarning("Warning", "An error occurred while deleting the task.")

def toggle_task():
    try:
        index = listbox.curselection()
        if index:
            task_text = listbox.get(index)
            if task_text.startswith("✓ "):
                task_text = task_text[2:]
            else:
                task_text = "✓ " + task_text
            listbox.delete(index)
            listbox.insert(index, task_text)
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")
    except:
        messagebox.showwarning("Warning", "An error occurred while marking the task as done.")

# Create the main window
window = tk.Tk()
window.title("To-Do List")
window.configure(bg="grey") 

# Entry widget to add tasks
entry = tk.Entry(window, width=50)
entry.pack(padx=10, pady=5, side=tk.TOP)

# Font for buttons
button_font = Font(family="Arial", size=12, weight="bold")

# Add Task button
add_button = tk.Button(window, text="Add Task", command=add_task, font=button_font)
add_button.pack(side=tk.LEFT, padx=5)

# Delete Task button
delete_button = tk.Button(window, text="Delete Task", command=delete_task, font=button_font)
delete_button.pack(side=tk.LEFT, padx=5)

# Done Task button
toggle_button = tk.Button(window, text="Done Task", command=toggle_task, font=button_font)
toggle_button.pack(side=tk.LEFT, padx=5)

# Listbox to display tasks
listbox = tk.Listbox(window, width=50)
listbox.pack(padx=10, pady=5)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link scrollbar to listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Start the Tkinter event loop
window.mainloop()