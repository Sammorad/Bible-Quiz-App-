from fasthtml.common import *
import random

Quiz = [{
        "id": 1,
        "question": "Who was the first king of Israel",
        "options": [
            "A. Saul",
            "B. David",
            "C. Solomon",
            "D. Samuel"
        ],
        "answer": "A"
    },
    {
        "id": 2,
        "question": "Who was the father of the twelve tribes of Israel",
        "options": [
            "A. Isaac",
            "B. Abraham",
            "C. Jacob",
            "D. Joseph"
        ],
        "answer": "C"
    },
    {
        "id": 3,
        "question": "Who was the father of the twelve tribes of Israel",
        "options": [
            "A. Isaac",
            "B. Abraham",
            "C. Jacob",
            "D. Joseph"
        ],
        "answer": "C"
    }]

app, rt = fast_app()

# Store the current question in a global variable
current_question = None

@rt("/")
def get():
    return Titled("Bible Quiz",
                  Button("Start Quiz",hx_get = "/question", hx_target = "#quiz_area")), Div(id = "quiz_area")


@rt("/question")
def question():
    global current_question
    current_question = random.choice(Quiz)
    return Div(current_question["question"], 
               *[Button(opt, hx_get = f"/answer/{opt}", hx_target = "#quiz_area") for opt in current_question["options"]],
               )

@rt("/answer/{opt}")
def answer(opt):
    global current_question
    
    if current_question:
        # Extract the letter from the option (e.g., "A" from "A. Saul")
        selected_answer = opt.split(".")[0].strip()
        is_correct = selected_answer == current_question["answer"]
        
        # Create feedback message
        feedback = Div(
            f"Your answer: {opt}",
            Div(f"{'Correct!' if is_correct else 'Wrong!'}", 
                style="color: green" if is_correct else "color: red"),
            Button("Next Question", hx_get="/question", hx_target="#quiz_area")
        )
        return feedback
    
    # If no current question, return to quiz
    return Div("Error: No question available", 
               Button("Try Again", hx_get="/question", hx_target="#quiz_area"))

serve()