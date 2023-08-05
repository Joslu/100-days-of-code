from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for data in question_data:
    question_bank.append(Question(data['text'], data['answer']))

quiz = Quiz(question_bank)

while quiz.still_questions():
    quiz.next_question()

print(f"You have completed the quiz 🎇🍾!!, your grade is: {quiz.get_grade()}")
