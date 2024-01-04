from Question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)


print("question bank questions")
print(question_bank[0].text, question_bank[0].answer)

quiz = QuizBrain(question_bank)
quiz.next_question()