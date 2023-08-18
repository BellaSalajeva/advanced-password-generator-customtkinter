from tkinter import *
import customtkinter
import random
import string

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title('Strong Password Generator')
root.iconbitmap()
root.geometry("600x400")


def generate_password():
    pwd_entry.delete(0, END)
    
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    min_length = int(my_entry.get())

    characters = letters
    include_numbers = check_var_num.get() == "on"
    include_special = check_var_sym.get() == "on"

    if include_numbers:
        characters += digits
    if include_special:
        characters += special
    
    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if include_numbers:
            meets_criteria = has_number
        if include_special:
            meets_criteria = meets_criteria and has_special
    
    pwd_entry.insert(0, password)

    save_password_txt(password)

# Checkboxes
def checkbox_event_num():
    print("checkbox toggled, current value:", check_var_num.get())

def checkbox_event_sym():
    print("checkbox toggled, current value:", check_var_sym.get())

# Copy to Clipboard
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pwd_entry.get())


def save_password_txt(password):
    with open('my_passwords.txt', 'a') as pw:
        pw.write("Password: " + password + "\n")


# Label at the Top
top_label = customtkinter.CTkLabel(root, text="Why do you need a strong password?\nSafety! A 14+ character password with at least one uppercase letter, number, and symbol takes 200 million years to crack.", font=("Roboto", 14), text_color="silver", wraplength=500)
top_label.pack(pady=20)


# Input Entry Box
entry_frame = customtkinter.CTkFrame(root, corner_radius=10)
entry_frame.pack(pady=10)

my_entry = customtkinter.CTkEntry(entry_frame, width=200, height=40, border_width=1, placeholder_text="Min. Password Length", text_color="silver")
my_entry.pack(pady=20, padx=20)
my_entry.grid(row=1, column=0, padx=10, pady=10)

check_var_num = customtkinter.StringVar(value="on")
checkbox_num = customtkinter.CTkCheckBox(entry_frame, text="Include numbers", command=checkbox_event_num, variable=check_var_num, onvalue="on", offvalue="off")
checkbox_num.grid(row=1, column=1, padx=10)

check_var_sym = customtkinter.StringVar(value="on")
checkbox_sym = customtkinter.CTkCheckBox(entry_frame, text="Include symbols", command=checkbox_event_sym, variable=check_var_sym, onvalue="on", offvalue="off")
checkbox_sym.grid(row=1, column=2, padx=10)


# Generate Button and Frame
gen_frame = customtkinter.CTkFrame(root, corner_radius=10)
gen_frame.pack(pady=10)

create_button = customtkinter.CTkButton(gen_frame, text="Generate", command=generate_password)
create_button.grid(row=2, column=1, pady=10, padx=10)


# Returned Password and Frame
pwd_frame = customtkinter.CTkFrame(root, corner_radius=10)
pwd_frame.pack(pady=20)

pwd_entry = customtkinter.CTkEntry(pwd_frame, width=200, height=40, border_width=1, text_color="silver", placeholder_text="Password:")
pwd_entry.pack(pady=20, padx=20)
pwd_entry.grid(row=3, column=0, padx=10, pady=10)


# Clip Button
clip_button = customtkinter.CTkButton(pwd_frame, text="Copy", command=clipper)
clip_button.grid(row=3, column=1, padx=10)


# Label at the Bottom
bot_label = customtkinter.CTkLabel(root, text="Generated passwords are also saved in my_passwords.txt.", font=("Roboto", 12), text_color="silver")
bot_label.pack()

root.mainloop()
