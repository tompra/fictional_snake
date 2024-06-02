import random
import tkinter as tk
from tkinter import messagebox

def generatePassword():
    try:
        number = int(number_input.get())
        length = int(length_input.get())
    except ValueError:
        messagebox.showerror("Invalid input.", 'Please enter valid numbers for the number and length of passwords.')
        return

    passwords = []
    
    for pwd in range(number):
        password = ''.join(random.choice(chars))
        for c in range(length):
            passwords.append(password)

def copyToClipboard(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo('Copied to clipboard', f"Password '{password}' copied to clipboard.")


def showPasswords(passwords):
    for widget in password_frame.winfo_children():
        widget.destroy()
        
    for password in passwords:
        password_label = tk.Label(password_frame, text=password, fg="white", cursor='pointer')
        password_label.pack()
        password_label.bind("<Button-1>", lambda e, p=password: copy_to_clipboard(p))



root = tk.Tk()
root.title("Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&)_.,?0123456789'

tk.Label(root, text='Choose the number of passwords to generate:', pady='10px').pack()
number_input = tk.Entry(root)
number_input.pack()

tk.Label(root, text="Choose your password length:", pady='10px').pack()
length_input = tk.Entry(root)
length_input.pack()

generate_button = tk.Button(root, text='Generate Password', command=generatePassword, pady='5px', padx='5px')
generate_button.pack(padx=20, pady=10)

password_frame = tk.Frame(root)
password_frame.pack()

root.mainloop()