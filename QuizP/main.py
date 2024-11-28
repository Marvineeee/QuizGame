quiz = {
    'basketball' : {
        'How many steps you can take per dribble? ' : "2",
        'How much is a layup worth? ' : "2",
        'How much is a 3pter worth? ' : "3",
        'Which NBA player has the best handle? ' : 'kyrie'
    },
    'food' : {
        'What is the best natural candy? ' : 'fruits',
        'Comfort food? ' : 'pizza',
        'Best fast food place? ' : 'chick fil a',
        'Best fruit? ' : 'grapes'
    }
}

def main():
    choice = str(input("(C)reate your own quiz or (Q)uiz?: "))[0].upper()
    match choice:
        case "C":
            answers = []
            questions = []

            quiz_name = str(input("Quiz Name?: ")).lower()
            add_questions = True
            while add_questions:
                question_answer_pair = str(input("Add your question & answer: ")).split(",")
                question, answer = question_answer_pair
                questions.append(question)
                answers.append(answer)

                print(questions, answers)
                more = str(input("Would you like too add more? (y/n) "))[0].lower()
                if more == "n":
                    add_questions = False
                    break
                elif more == "y":
                    continue
            packed = dict(zip(questions, answers))
            print("Packed Quiz: ", packed)
            quiz[quiz_name] = packed

            return main()

        case "Q":
            selected_quiz = ''
            while selected_quiz not in quiz:
                selected_quiz = str(input("Select A Quiz: ")).lower()

            answers = []

            if selected_quiz in quiz:
                for question, answer in quiz[selected_quiz].items():
                    test = str(input(question)).lower()
                    if test == answer:
                        answers.append(answer)
                
                grade = grade_system(quiz, selected_quiz, answers)
                print(f"You have scored an {grade}!")

def grade_system(quiz, selected_quiz, answers):
    number_of_questions = len(quiz[selected_quiz])
    number_of_answers = len(answers)
    answers.clear()
    return int(number_of_answers / number_of_questions * 100)

main()

# Project done, fix string for custom quiz.