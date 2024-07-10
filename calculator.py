import tkinter as tk

def btns(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "del":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Setting up the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("250x400")
window.configure(bg="gray")

# Create an input field (Entry widget)
entry = tk.Entry(window, font=("Arial", 20), bd=5)
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=10, sticky="nsew")

# Define the buttons and their layout
buttons = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    ".", "0", "=", "/",
    "del"
]

# Function to create and place buttons
def create_button(text, row, col):
    btn = tk.Button(window, text=text, font=("Arial", 15), padx=10, pady=10, width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", btns)

# Loop to create buttons
index = 0
for row in range(1, 6):
    for col in range(4):
        create_button(buttons[index], row, col)
        index += 1
        if index >= len(buttons):
            break
    if index >= len(buttons):
        break

# Configure rows and columns to expand with window resizing
for i in range(1, 6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Run the main loop
window.mainloop()