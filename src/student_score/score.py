from fasthtml.common import *
from fasthtml.common import Request


app, rt = fast_app()

def student_score(score):
    try:
        score = float(score)
        if score > 69:
            grade = "A, Excellent"
        elif score >= 60:
            grade = "B, Very Good"
        elif score >= 50:
            grade = "C, Good"
        elif score >= 40:
            grade = "D, pass"
        else:
            grade = "F, Fail"
        return grade
    except ValueError:
        return "Please enter a valid number"

@rt("/")
def main():
    return Div(
        Titled("Student Score Grading System",
            Form(
                Input("score_input", "What is the student score: "),
                Button("Get Grade", type="submit"),
                hx_post = "/get_grade", hx_target = "#grade"
            )
        )
    )

@rt("/get_grade")
def get_grade():
    score = Request.form.get("score_input")
    grade = student_score(score)
    return Div(
        Titled("Student Score Grading System",
            Form(
                Input("score_input", "What is the student score: "),
                Button("Get Grade", type="submit"),
                action="/get_grade", hx_target = "grade"
            ),
            Div(f"Grade: {grade}")
        )
    )

serve()
