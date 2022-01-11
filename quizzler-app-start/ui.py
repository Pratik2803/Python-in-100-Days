from tkinter import *
import quiz_brain, config


class QuizzerInterface:
    def __init__(self, quiz: quiz_brain):
        self.quiz = quiz

        self.main_window = Tk()
        self.main_window.title('Quizzer')
        self.main_window.config(bg=config.THEME_COLOR, padx=20, pady=20)
        right_img = PhotoImage(file='./images/true.png')
        wrong_img = PhotoImage(file='./images/false.png')
        self.score = 0

        self.score_label = Label(self.main_window, text=f"Score: {self.score}", fg='white', bg=config.THEME_COLOR)

        self.canvas = Canvas(self.main_window, width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="text",
            width=280,
            font=('Ariel', 15, 'italic'),
            fill=config.THEME_COLOR,
        )

        self.right_btn = Button(self.main_window, image=right_img, bd=0, highlightthickness=0)
        self.wrong_btn = Button(self.main_window, image=wrong_img, bd=0, highlightthickness=0)

        self.score_label.grid(column=1, row=0, sticky=E)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=20)
        self.right_btn.grid(column=0, row=2)
        self.wrong_btn.grid(column=1, row=2)
        self.set_question()
        self.right_btn.config(command=self.click_right)
        self.wrong_btn.config(command=self.click_wrong)

        self.main_window.mainloop()

    def set_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text='GAME  FINISHED')
            self.right_btn.config(state=DISABLED)
            self.wrong_btn.config(state=DISABLED)

    def click_right(self):
        answer = self.quiz.current_question_answer()
        if answer == 'True':
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.main_window.after(1000, self.set_question)

    def click_wrong(self):
        answer = self.quiz.current_question_answer()
        if answer == 'False':
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.main_window.after(1000, self.set_question)
