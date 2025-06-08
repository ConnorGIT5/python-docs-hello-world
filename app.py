from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Page is working correctly. \n Page takes some time to update content even after the logs confirm that build/deploy was been successfully completed."
