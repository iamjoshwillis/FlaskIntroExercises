from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/welcome")
def welcome_page():
    return "Welcome!"

@app.route("/welcome/home")
def welcomehome_page():
    return "Welcome Home!"

@app.route("/welcome/back")
def welcomeback_page():
    return "Welcome Back!"