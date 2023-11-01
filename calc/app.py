# Put your app in here.
from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def int_add():
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a + b)


@app.route("/sub")
def sub():
    """Substract b from a."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a - b)


@app.route("/mult")
def mult():
    """Multiply a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a * b)


@app.route("/div")
def div():
    """Divide a by b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a / b)


# Further Study Portion

math_methods = {"add": add, "sub": sub, "mult": mult, "div": div}


@app.route("/math/<method>")
def calc(method):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    calculated = math_methods[method](a, b)
    return str(calculated)
