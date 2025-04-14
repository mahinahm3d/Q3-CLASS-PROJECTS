import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip
from zxcvbn import zxcvbn

def generate_password(length):
    if length < 4:
        raise ValueError("Password must be at least 4 characters long.")
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        secrets.choice(upper),
        secrets.choice(lower),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    all_chars = upper + lower + digits + symbols
    password += [secrets.choice(all_chars) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def generate_and_display():
    try:
        length = int(length_entry.get())
        num = int(number_entry.get())
        passwords = [generate_password(length) for _ in range(num)]
        result_text.delete("1.0", tk.END)
        for i, pwd in enumerate(passwords, 1):
            result_text.insert(tk.END, f"{i}. {pwd}\n")
        global last_passwords
        last_passwords = passwords
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def auto_clear_clipboard(seconds):
    root.after(seconds * 1000, lambda: pyperclip.copy(''))

def copy_password():
    selected = result_text.get("insert linestart", "insert lineend").strip()
    if selected and '. ' in selected:
        pwd = selected.split('. ', 1)[1]
        pyperclip.copy(pwd)
        auto_clear_clipboard(15)
        strength = zxcvbn(pwd)
        score = strength['score']
        warn = strength['feedback']['warning']
        messagebox.showinfo("Copied", f"Password copied!\nStrength Score: {score}/4\n{warn or ''}")
    else:
        messagebox.showwarning("No password selected", "Click a line first.")

# GUI setup
root = tk.Tk()
root.title("🔐 Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Number of Passwords:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1, padx=10, pady=5)

generate_btn = tk.Button(root, text="Generate", command=generate_and_display)
generate_btn.grid(row=2, column=0, columnspan=2, pady=10)

result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

copy_btn = tk.Button(root, text="Copy Selected", command=copy_password)
copy_btn.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
