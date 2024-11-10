import random

def get_difficulty_range(level):
    if level == 1:
        return 1, 5
    elif level == 2:
        return 1, 10
    elif level == 3:
        return 5, 15
    else:
        print("Invalid difficulty level.")
        return None

def ask_questions(level, num_questions=5):
    correct_answers = 0
    min_range, max_range = get_difficulty_range(level)

    if min_range is None:
        return 0

    for i in range(num_questions):
        a = random.randint(min_range, max_range)
        b = random.randint(min_range, max_range)
        answer = int(input(f"What is {a} * {b}?\n> "))

        if answer == a * b:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong. The correct answer is: {a * b}")

    return correct_answers

def evaluate_performance(correct_answers, total_questions):
    score_percentage = (correct_answers / total_questions) * 100
    print(f"Your result: {correct_answers} out of {total_questions} ({score_percentage:.2f}%).")

    if score_percentage >= 90:
        print("Excellent! You have a high level of knowledge.")
    elif score_percentage >= 70:
        print("Good! There are some mistakes, but you did well.")
    elif score_percentage >= 50:
        print("Not bad, but you need a bit more practice.")
    else:
        print("You need to practice more.")

print("Choose difficulty level (1 - easy, 2 - medium, 3 - hard):")
level = int(input("Enter difficulty level: "))
num_questions = 5

correct_answers = ask_questions(level, num_questions)
evaluate_performance(correct_answers, num_questions)