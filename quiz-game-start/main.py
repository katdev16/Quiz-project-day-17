from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    # question_bank  = Question()
    text = i["text"]
    answer = i["answer"]
    new_question=  Question(text,answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz.next_question()

