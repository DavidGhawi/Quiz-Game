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
    1: "red",
    2: "Cardiff",
    3: "10"
}

global correctcounter


# ADD ALL APP ROUTES HERE

@app.route("/approved_questions", methods=["GET"])
def returnDir():
    if request.method == 'GET':
        print("getting directory.")
        return json.dumps(approved_questions);

@app.route("/Useranswer", methods=["post"])
def checkans():
    global correctcounter
    print("Checking answer")
    if request.method == "POST":
        answer = request.form["answer"]
        print (answer + "IT WORKED")
        if answer == approved_answers[1]:
            correctcounter += 1
    return answer

@app.route("/LoadQuestions", methods=["GET"])
def returnQuestions():
    if request.method == 'GET':
        print("getting questions")
        return json.dumps(approved_questions);
















if __name__ == "__main__":
    app.run(debug=True)
