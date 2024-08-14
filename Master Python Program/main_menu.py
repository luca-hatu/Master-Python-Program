import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import math

def run_program(program_path):
    if os.path.isfile(program_path):
        try:
            subprocess.run(['python', program_path], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to execute {program_path}: {e}")
    else:
        messagebox.showerror("Error", f"File {program_path} does not exist!")

def create_icon_button(root, image_path, program_path, title, x, y):
    img = Image.open(image_path)
    img = img.resize((80, 80), Image.LANCZOS)
    icon = ImageTk.PhotoImage(img)

    btn = tk.Button(root, image=icon, command=lambda: run_program(program_path), borderwidth=0, bg="white")
    btn.image = icon
    btn.place(x=x, y=y, anchor=tk.CENTER)

    label = tk.Label(root, text=title, bg="lightgray", font=("Arial", 10))
    label.place(x=x, y=y+50, anchor=tk.CENTER)

    def on_enter(event):
        btn.config(bg="lightblue")

    def on_leave(event):
        btn.config(bg="white")

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

def main():
    root = tk.Tk()
    root.title("Program Launcher")
    root.geometry("600x600")
    root.config(bg="lightgray")

    launcher_icon = "swiss-army-knife.ico" 
    root.iconbitmap(launcher_icon)

    radius = 200
    center_x = 300
    center_y = 300
    num_buttons = 7

    programs = [
        {'name': 'Unit Converter', 'icon': 'Unit Converter/icon.ico', 'path': 'Unit Converter/unit_converter.py'},
        {'name': 'Currency Converter', 'icon': 'Currency Converter/exchange.ico', 'path': 'Currency Converter/currency_converter.py'},
        {'name': 'Text Encryption', 'icon': 'Encryption Tool/encryption.png', 'path': 'Encryption Tool/encryption_tool.py'},
        {'name': 'Secure Notes', 'icon': 'Secure Notes/notepad.png', 'path': 'Secure Notes/secure_notes.py'},
        {'name': 'File Locker', 'icon': 'File Locker/lock.png', 'path': 'File Locker/file_locker.py'},
        {'name': 'Password Manager', 'icon': 'Password Manager/password_manager.png', 'path': 'Password Manager/password_manager.py'},
        {'name': 'Password Generator', 'icon': 'Password Generator/password_generator.png', 'path': 'Password Generator/password_generator.py'},
    ]

    for i, program in enumerate(programs):
        angle = 2 * math.pi * i / num_buttons
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        create_icon_button(root, program['icon'], program['path'], program['name'], x, y)

    root.mainloop()
if __name__ == "__main__":
    main()
