from tkinter import *
from ui import UI

LOGO_FILE = './logo.png'
APP_TITLE = "Password Manager"

main_window = Tk()
main_window.title(APP_TITLE)
main_window.config(padx=50, pady=50)

# Logo Image Set-Up
canvas = Canvas(main_window, width=200, height=200)

logo_image = PhotoImage(file=LOGO_FILE)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

APP_UI = UI(main_window)
APP_UI.focus_website_text_box()
APP_UI.click_generate_password()

main_window.mainloop()
