from question_model import Question
from data import Data
from quiz_brain import QuizBrain
from ui import QuizzerInterface

questions = Data()

question_bank = []
for question in questions.question_data():
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
app_ui = QuizzerInterface(quiz)

