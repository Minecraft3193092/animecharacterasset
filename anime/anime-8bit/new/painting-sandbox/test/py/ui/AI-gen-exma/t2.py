import tkinter as tk
from tkinter import messagebox

def on_click():
    messagebox.showinfo("Success", "Button clicked successfully!")

# Initialize the main root window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("400x200")

# Create and position a text label
label = tk.Tk.Label if not hasattr(tk, 'Label') else tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Create and position an action button
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# Start the continuous event listening loop
root.mainloop()