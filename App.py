from flask import Flask
from core.Action import Action

app = Flask(__name__)


@app.route("/")
def default():
    return "None"

@app.route("/q")
def action():
    myAction = Action()
    myAction.exec()
    return "action done"

if __name__ == "__main__":
    app.run()