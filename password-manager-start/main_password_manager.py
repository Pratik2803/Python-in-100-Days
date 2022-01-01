from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint

FONT = ("Calibri", 10)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for char in range(randint(8, 10))]
    symbol_list = [choice(symbols) for char in range(randint(2, 4))]
    numbers_list = [choice(numbers) for char in range(randint(2, 4))]

    password_list = letter_list + symbol_list + numbers_list

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Empty Field', message="Fields must be filled")
    else:
        save_data = messagebox.askyesno(title="Confirmation", message="Do you want to proceed?")
        if save_data:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            with open(file='./password.txt', mode='a') as file:
                file.write(f'{website}  | {email}  | {password}\n')

            messagebox.showinfo(title="Password Manager", message="Password is saved successfully")
        else:
            messagebox.showinfo(title="Password Manager", message="Password is Not saved")


# ---------------------------- UI SETUP ------------------------------- #

# main window
main_window = Tk()
main_window.title("Password Manager")
main_window.config(padx=50, pady=50)

# logo image
canvas = Canvas(main_window, width=200, height=200)
logo_image = PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website label and text box
website_label = Label(text='Website: ', font=FONT)
website_label.grid(row=1, column=0, sticky="W")

website_entry = Entry(width=35, font=FONT)
website_entry.focus_set()
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")

# Email label and text box
email_label = Label(text='Email/Username: ', font=FONT)
email_label.grid(row=2, column=0, sticky="W")

email_entry = Entry(width=35, font=FONT)
email_entry.insert(0, 'Pratik_adr@live.com')
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")

# Password label, text box and button
password_label = Label(text='Password: ', font=FONT)
password_label.grid(row=3, column=0, sticky="W")

password_entry = Entry(width=21, font=FONT)
password_entry.grid(row=3, column=1, sticky="W")

generate_password_btn = Button(text='Generate Password', font=FONT, command=gen_password)
generate_password_btn.grid(row=3, column=2, sticky="W")

# Add button
add_btn = Button(text='ADD', font=FONT, width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky="W")

main_window.mainloop()
