from random import choice, shuffle, randint
from tkinter import END

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class Password_Generate:

    def __init__(self, password_entry):
        self.password_entry = password_entry

    def gen_password(self):
        letter_list = [choice(LETTERS) for char in range(randint(8, 10))]
        symbol_list = [choice(SYMBOLS) for char in range(randint(2, 4))]
        numbers_list = [choice(NUMBERS) for char in range(randint(2, 4))]

        password_list = letter_list + symbol_list + numbers_list

        shuffle(password_list)
        password = "".join(password_list)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
