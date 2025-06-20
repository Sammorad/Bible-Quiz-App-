import random
import json

# Improved Quiz structure with correct answers included
FILENAME = "C:/Users/hp/Desktop/dejiowoeye/data_analysis/my_project/bible_quiz_app/bible_quiz_app.json"

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
        return quiz

def users_answers(item):
    """Get the user's answer and check if it's correct"""
    answer = input("Answer: ").strip().upper()
    if answer in ["A", "B", "C", "D"]:
        correct_answer = item["answer"]
        if answer == correct_answer:
            print("You are correct! Great Job")
        else:
            print(f"That's not quite right. The correct answer is '{correct_answer}'. Keep trying!")
    else:
        print("Oops! That's not a valid option. Please enter A, B, C, or D.")

def validate_question_number(question_number, quiz):
    while True:
        if question_number < 1 or question_number > len(quiz):
            print(f"Invalid question number, kindly enter a number between 1 and {len(quiz)}")
            quest = input("re-enter your question number or enter q to quit: ")
            if quest == "q":
                break
            else:
                return quest
       
        else:
            confirm_number = input(f"Are you sure you want to modify or delete question {question_number}? Enter yes or no :").strip().lower()
            if confirm_number == "yes":
                return question_number
            else:
                print("Operation cancelled")
                raise ValueError("Operation cancelled by user")

def update_new_question():
    """Add question to question, options and answer"""
    new_question = input("Enter the new question: ")
    options = []
    for i in range(4):
        option = input(f"Enter option {chr(65 + i)}: ")
        options.append(option)
    new_answer = input("Enter the correct answer (A, B, C, or D): ").strip().upper()
    return {
        "question": new_question,
        "options": options,
        "answer": new_answer}
    

def add_question_and_answer():
    """Add a new question and answer to the quiz"""
    new_question = update_new_question()
    quiz = load_quiz()
    quiz.append({"question": new_question["question"], "options": new_question["options"], "answer": new_question["answer"]})
    save_quiz(quiz)
    print("Question added successfully!")




def modify_question():
    """Modify a question in the quiz"""
    quiz = load_quiz()
    if not quiz:
        print("No quiz available to modify.")
        return
    try:
        question_number = int(input("Enter the question number to modify: "))
        validate_number = validate_question_number(question_number, quiz)
        new_question = update_new_question()
        quiz[validate_number - 1]["question"] = new_question["question"]
        quiz[validate_number - 1]["options"] = new_question["options"]
        quiz[validate_number - 1]["answer"] = new_question["answer"]
        save_quiz(quiz)
        print("Question modified successfully!")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def delete_question():
    """Delete a question from the quiz"""
    quiz = load_quiz()
    if not quiz:
        print("No quiz available to delete.")
        return
    try:
        question_number = int(input("Enter the question number to delete: "))
        validate_number = validate_question_number(question_number, quiz)
        del quiz[validate_number - 1]
        save_quiz(quiz)
        print("Question deleted successfully")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    


def main():
    """Main function to initialize and manage the quiz workflow."""
    print("Are you an admin or a user?")
    print("Enter 'admin' to add a question and answer")
    print("Enter 'user' to take the quiz")
    print("Enter 'q' to quit")
    action = input("Enter your choice: ").strip().lower()
    if action == "admin":
        while True:
            print("Enter 'add' to add a question and answer")
            print("Enter 'modify' to modify a question")
            print("Enter 'delete' to delete a question")
            print("Enter 'q' to quit")
            admin_action = input("Enter your choice: ").strip().lower()
        
            if admin_action == "add":
                add_question_and_answer()
            elif admin_action == "modify":
                modify_question()
            elif admin_action == "delete":
                delete_question()
            elif admin_action == "q":
                return
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


main()
