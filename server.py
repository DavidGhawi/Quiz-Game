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
@app.route("/inputed_data")

@app.route("/ditionary_display")
def returnDir():
    if request.method == 'GET':
        print("getting directory.")
        return json.dumps(submitted_questions);

@app.route("/submitted_display", methods = ["POST"])
def addQuestion():
    print('processing Data')
    message ='already there'
    if request.method == 'POST':
        questionID = request.form['questionID']
        print (f"questionID = {questionID}")
        message = 'ok'
        keyID = len(approved_questions) + 1
        print (keyID)
        print (submitted_questions)
        print (approved_questions)
        questionID = int(questionID)
        approved_questions[keyID] = submitted_questions[questionID]
        del submitted_questions[questionID]
        approved_answers[keyID] = submitted_answers[questionID]
        del submitted_answers[questionID]
        print (f" this is approved question{approved_questions}")
    return message




















if __name__ == "__main__":
    app.run(debug=True)
