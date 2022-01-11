from html import unescape


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:

        self.current_question = self.question_list[self.question_number]
        current_question_text = unescape(self.current_question.text)
        self.question_number += 1
        return f'Q.{self.question_number}: {current_question_text}'

    def current_question_answer(self) -> bool:
        correct_answer = self.current_question.answer
        return correct_answer

