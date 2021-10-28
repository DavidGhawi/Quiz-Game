import os
import json
from flask import Flask, redirect, request,render_template, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

submitted_questions = {
    1: "What color is a london bus?",
    2: "What speed does a snake flap its wings?"
}

submitted_answers = {
    1: "red",
    2: "23 speed"
}

approved_questions = {
    1: "What color is a coke can?",
    2: "What is the capital city of Wales?",
    3: "How many fingers does a human have?"
}

approved_answers = {
    1:"red",
    2 :"Cardiff",
    3: "10"
}


# ADD ALL APP ROUTES HERE















@app.route("/AddUserQuestion", methods=["POST"])
def addUserQuestion():
    print("Request to add a question made")
    if request.method == "POST":
        question = request.form["question"]
        answer = request.form["answer"]
        message = "This question has already been submitted"
        if not(question in submitted_questions.values() or question in approved_questions.values()):
            message = "Your question has been submitted. Please do not submit it again"
            question_number = len(submitted_questions) +1
            submitted_questions[question_number] = question
            submitted_answers[question_number] = answer
        print("QUESTIONS!")
        print(submitted_questions)
        print("ANSWERS!")
        print(submitted_answers)
    return message




if __name__ == "__main__":
    app.run(debug=True)
