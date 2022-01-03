from tkinter import *
from password_generator import Password_Generate
from tkinter import messagebox
import json

FONT = ("Calibri", 10)

# Labels Text
WEBSITE_LABEL = 'Website: '
EMAIL_LABEL = 'Email/Username: '
PASSWORD_LABEL = 'Password: '

# Buttons Text
GEN_PASS_BTN = 'Generate Password'
ADD_BTN = 'ADD'
SEARCH_BTN = 'Search'

DEFAULT_EMAIL = 'Pratik_adr@live.com'

FILE_LOC = './data.json'


class UI:

    def __init__(self, main_window):
        self.main_window = main_window

        # Website label and text box
        self.website_label = Label(text=WEBSITE_LABEL, font=FONT)
        self.website_label.grid(row=1, column=0, sticky="W")

        self.website_entry = Entry(width=28, font=FONT)
        self.website_entry.grid(row=1, column=1, sticky="W")

        # Search Button
        self.search_btn = Button(text=SEARCH_BTN, font=FONT, command=self.click_search, bd=1)
        self.search_btn.grid(row=1, column=2, sticky="W")

        # Email label and text box
        self.email_label = Label(text=EMAIL_LABEL, font=FONT)
        self.email_label.grid(row=2, column=0, sticky="W")

        self.email_entry = Entry(width=35, font=FONT)
        self.email_entry.insert(0, DEFAULT_EMAIL)
        self.email_entry.grid(row=2, column=1, columnspan=2, sticky="W")

        # Password label, text box and button
        self.password_label = Label(text=PASSWORD_LABEL, font=FONT)
        self.password_label.grid(row=3, column=0, sticky="W")

        self.password_entry = Entry(width=28, font=FONT)
        self.password_entry.grid(row=3, column=1, sticky="W")

        self.generate_password_btn = Button(text=GEN_PASS_BTN, font=FONT, bd=1)
        self.generate_password_btn.grid(row=3, column=2, sticky="W")

        # Add button

        self.add_btn = Button(text=ADD_BTN, font=FONT, width=36, command=self.save_password)
        self.add_btn.grid(row=4, column=1, columnspan=2, sticky="W")

    # Sets focus on website text box
    def focus_website_text_box(self):
        self.website_entry.focus_set()

    # Generate Password Button functionality
    def click_generate_password(self):
        self.generate_password_btn['command'] = Password_Generate(self.password_entry).gen_password

    # Add button logic
    def save_password(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            self.show_info(title='Empty Field', message="Fields must be filled")
        else:
            save_data = messagebox.askyesno(title="Confirmation", message="Do you want to proceed?")
            if save_data:

                self.website_entry.delete(0, END)
                self.password_entry.delete(0, END)
                try:
                    with open(file=FILE_LOC, mode='r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    with open(file=FILE_LOC, mode='w') as file:
                        json.dump(new_data, file, indent=4, sort_keys=True)
                else:
                    data.update(new_data)
                    with open(file=FILE_LOC, mode='w') as file:
                        json.dump(data, file, indent=4, sort_keys=True)

                self.show_info(title="Password Manager", message="Password is saved successfully")
            else:
                self.show_info(title="Password Manager", message="Password is Not saved")

    def show_info(self, title, message):
        messagebox.showinfo(title=title, message=message)

    # Search button functionality
    def click_search(self):
        website = self.website_entry.get().strip()

        if len(website) == 0:
            self.show_info(title='Error', message="Provide Website Name")
        else:

            try:
                with open(file=FILE_LOC, mode='r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                self.show_info(title='Error', message="No Record is Saved")
            else:
                if website in data:
                    self.show_info(title="Record Exists", message=f"email: {data[website]['email']}\n password: {data[website]['password']}")
                else:
                    self.show_info(title='Error', message='No record Exists')
