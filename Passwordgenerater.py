import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password():
    length = int(length_var.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    char_set = string.ascii_lowercase
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_special:
        char_set += string.punctuation

    password = ''.join(random.choice(char_set) for _ in range(length))
    password_var.set(password)

def copy_password():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Password Generator", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")


length_var = tk.StringVar(value='12')
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()
password_var = tk.StringVar()

# Widgets

tk.Label(root, text="Password Length:").pack(pady=5)
tk.Entry(root, textvariable=length_var).pack(pady=5)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack(pady=5)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(pady=5)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Entry(root, textvariable=password_var, state='readonly').pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=10)

root.mainloop()