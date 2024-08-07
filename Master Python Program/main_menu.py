import os
import subprocess

def display_menu():
    print("Select a program to run:")
    print("1. Unit Converter")
    print("2. Currency Converter")
    print("3. Text Encryption")
    print("4. Secure Notes")
    print("5. File Locker")
    print("6. Password Manager")
    print("7. Password Generator")
    print("0. Exit")

def run_program(choice):
    programs = {
        '1': 'Unit Converter/unit_converter.py',
        '2': 'Currency Converter/currency_converter.py',
        '3': 'Encryption Tool/encryption_tool.py',
        '4': 'Secure Notes/secure_notes.py',
        '5': 'File Locker/file_locker.py',
        '6': 'Password Manager/password_manager.py',
        '7': 'Password Generator/password_generator.py',
    }

    if choice in programs:
        program_path = programs[choice]
        subprocess.run(['python', program_path])
    else:
        print("Invalid choice!")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '0':
            print("Exiting...")
            break
        run_program(choice)

if __name__ == "__main__":
    main()
