from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Viewing the staging branch version. TEST 3"
