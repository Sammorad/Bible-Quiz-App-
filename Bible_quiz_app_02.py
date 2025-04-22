import random
import json

# Improved Quiz structure with correct answers included
FILENAME = "C:/Users/hp/Desktop/dejiowoeye/Data Analysis/my_project/bible_quiz_app/bible_quiz_app.json"

def load_quiz():
    """Read the quiz from the file"""
    try:
        with open(FILENAME, "r") as file:
            quiz = json.load(file)
            return quiz
    except FileNotFoundError:
        print("Quiz file not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding the quiz file.")
        return []


def save_quiz(quiz):
    """Write the quiz to the file"""
    with open(FILENAME, "w") as file:
        json.dump(quiz, file, indent=4)

def users_answers(item):
    """Get the user's answer and check if it's correct"""
    answer = input("Answer: ").strip().upper()
    correct_answer = item["answer"]
    if answer == correct_answer:
        print("You are correct!")
    else:
        print(f"Wrong Answer, the correct answer is '{correct_answer}'")
def add_question_and_answer():
    """Add a new question and answer to the quiz"""
    question = input("Enter the question: ")
    options = []
    for i in range(4):
        option = input(f"Enter option {chr(65 + i)}: ")
        options.append(option)
    answer = input("Enter the correct answer (A, B, C, or D): ").strip().upper()
    quiz = load_quiz()
    quiz.append({"question": question, "options": options, "answer": answer})
    save_quiz(quiz)
    print("Question added successfully!")

def bible_quiz():
    """Main function to initialize and manage the quiz workflow."""
    print("Are you an admin or a user?")
    print("Enter 'admin' to add a question and answer")
    print("Enter 'user' to take the quiz")
    print("Enter 'q' to quit")
    action = input("Enter your choice: ").strip().lower()
    if action == "admin":
        add_question_and_answer()
    elif action == "user":
        print("Welcome to the Beginners Bible Quiz")
        print("Return answers in form of A, B, C, or D")
        action = input("Enter 'yes' to start quiz or 'q' to quit: ").strip().lower()
        if action == "yes":
            try:
                number_of_quest = int(input("How many questions will you answer: "))
                if number_of_quest <= 0:
                    print("Please enter a positive number.")
                    return
            except ValueError:
                print("Invalid input. Please enter a number.")
                return

        quiz = load_quiz()
        if not quiz:
            print("No quiz available to load.")
            return

        for _ in range(number_of_quest):
            item = random.choice(quiz)
            print(item["question"])
            for option in item["options"]:
                print(option)
            users_answers(item)

bible_quiz()