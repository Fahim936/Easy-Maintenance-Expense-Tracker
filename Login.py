import tkinter as tk
from tkinter import messagebox
import os

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        # If login is successful, destroy the login window and open main.py
        root.destroy()
        os.system('main.py')
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Create the login window
root = tk.Tk()
root.title("Login")

# Add the username and password labels and entry fields
tk.Label(root, text="Username").grid(row=0)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)
tk.Label(root, text="Password").grid(row=1)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Add the login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(columnspan=2)

# Start the main event loop
root.mainloop()
