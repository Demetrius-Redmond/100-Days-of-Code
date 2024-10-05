from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for current_place in question_data:
    question = Question(current_place["text"], current_place["answer"])
    question_bank.append(question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    if False:
        break
    else:
        quiz.next_question()
quiz.complete()


