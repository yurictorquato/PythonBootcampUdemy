from quiz_brain import QuizBrain
from question_model import Question
from data import question_data


def main():
    question_bank = []

    for item in question_data:
        question_text = item["text"]
        question_answer = item["answer"]
        new_question = Question(question_text, question_answer)

        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()
        print()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

if __name__ == '__main__':
    main()
