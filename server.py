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

correctcounter = 0
questioncounter = 1


# ADD ALL APP ROUTES HERE

@app.route("/approved_questions", methods=["GET"])
def returnDir():
    if request.method == 'GET':
        print("getting directory.")
        return json.dumps(approved_questions);

@app.route("/Useranswer", methods=["post"])
def checkans():
    global correctcounter
    global questioncounter
    print (correctcounter)
    print("Checking answer")
    if request.method == "POST":
        answer = request.form["answer"]
        print (answer + " IT WORKED")
        print ("the answer should be: " + approved_answers[questioncounter])
        if answer == approved_answers[questioncounter]:
            correctcounter += 1
            print (correctcounter)
        questioncounter += 1

    return answer

@app.route("/LoadQuestions", methods=["GET"])
def returnQuestions():
    if request.method == 'GET':
        print("getting questions")
        return json.dumps(approved_questions);












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
























































@app.route("/ditionary_display")
def returnDir():
    if request.method == 'GET':
        return json.dumps(submitted_questions);

@app.route("/submitted_display", methods = ["POST"])
def addQuestion():
    print('processing Data')
    message ='already there'
    if request.method == 'POST':
        questionID = request.form['questionID']
        message = 'ok'
        keyID = len(approved_questions) + 1
        questionID = int(questionID)
        approved_questions[keyID] = submitted_questions[questionID]
        del submitted_questions[questionID]
    return message

@app.route("/actualques_display")
def returnQues():
    print("getting ques")
    if request.method == 'GET':
        print("getting actual question")
        return json.dumps(approved_questions);

@app.route("/remove_question", methods = ["POST"])
def remove_question():
    message ='already there'
    if request.method == 'POST':
        questionID = request.form['questionID']
        message = 'ok'
        questionID = int(questionID)
        print (questionID)
        del submitted_questions[questionID]
    return message

@app.route("/remove_actual_question", methods = ["POST"])
def removequestionactual():
    message ='already there'
    if request.method == 'POST':
        questionID = request.form['questionID']
        message = 'ok'
        print (questionID)
        questionID = int(questionID)
        print(questionID)
        del approved_questions[questionID]
    return message

if __name__ == "__main__":
    app.run(debug=True)
