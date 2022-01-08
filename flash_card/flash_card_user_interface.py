from tkinter import *
import pandas as pd
from random import choice
from utility import words_to_learn_csv


class AppUi:
    BACKGROUND_COLOR = "#B1DDC6"

    try:
        french_english_words = pd.read_csv("./data/words_to_learn.csv").to_dict(orient='records')
    except FileNotFoundError:
        french_english_words = pd.read_csv("./data/french_words_copy.csv").to_dict(orient='records')


    def __init__(self, main_window):
        # Main Window Config
        self.main_window = main_window
        self.main_window.title('Flashy')
        self.main_window.config(bg=AppUi.BACKGROUND_COLOR, padx=50, pady=50)
        self.flip = self.main_window.after(3000, self.flip_card)

        # Images
        self.french_flash_card_img = PhotoImage(file='./images/card_front.png')
        self.english_flash_card_img = PhotoImage(file='./images/card_back.png')
        self.wrong_btn_img = PhotoImage(file='./images/wrong.png')
        self.correct_btn_img = PhotoImage(file='./images/right.png')

        # Flash Card Config
        self.canvas = Canvas(width=800, height=526, bg=AppUi.BACKGROUND_COLOR, highlightthickness=0)
        self.img = self.canvas.create_image(410, 275, image=self.french_flash_card_img)
        self.title = self.canvas.create_text(400, 150, text='French', font='Ariel 40 italic')
        self.french_word = self.canvas.create_text(400, 300, text='histoire', font='Ariel 60 bold')
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Buttons
        self.correct_btn = Button(image=self.correct_btn_img, highlightthickness=0, bd=0, command=self.click_right_btn)
        self.correct_btn.grid(row=1, column=1, pady=50)

        self.wrong_btn = Button(image=self.wrong_btn_img, highlightthickness=0, bd=0, command=self.click_wrong_btn)
        self.wrong_btn.grid(row=1, column=0, pady=50)
        self.click_wrong_btn()

    # click wrong button
    def click_wrong_btn(self):
        self.main_window.after_cancel(self.flip)
        self.french_english_word = choice(AppUi.french_english_words)
        self.canvas.itemconfig(self.img, image=self.french_flash_card_img)
        self.canvas.itemconfig(self.title, text='French', fill='black')
        self.canvas.itemconfig(self.french_word, text=self.french_english_word['French'], fill='black')
        self.flip=self.main_window.after(3000, self.flip_card)

    # click right button
    def click_right_btn(self):
        self.main_window.after_cancel(self.flip)
        AppUi.french_english_words.remove(self.french_english_word)
        self.french_english_word = choice(AppUi.french_english_words)
        self.canvas.itemconfig(self.img, image=self.french_flash_card_img)
        self.canvas.itemconfig(self.title, text='French', fill='black')
        self.canvas.itemconfig(self.french_word, text=self.french_english_word['French'], fill='black')
        self.flip=self.main_window.after(3000, self.flip_card)
        words_to_learn_csv(AppUi.french_english_words)

    # flip card

    def flip_card(self):
        card_type = self.canvas.itemcget(self.title, 'text')

        if card_type == 'French':
            self.canvas.itemconfig(self.img, image=self.english_flash_card_img)
            self.canvas.itemconfig(self.title, text='English', fill='white')
            self.canvas.itemconfig(self.french_word, text=self.french_english_word['English'], fill='white')
