from flask import Flask
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        scores_file = open(SCORES_FILE_NAME, 'r')
        current_score = scores_file.read()
        scores_file.close()

        return """
        <html>
        <head><title>Scores Game</title></head>
        <body><h1>The score is: <div id="score">{SCORE}</div></h1></body>
        </html>
        """.format(SCORE=current_score)
    except:
        return """
        <html>
        <head><title>Scores Game</title></head>
        <body><h1>An error occured: <div id="score" style="color:red">{ERROR}</div></h1></body>
        </html>
        """.format(ERROR=BAD_RETURN_CODE)