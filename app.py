from flask import Flask, request,render_template
from fdm import solve_heat_equation
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate")
def calculate():
    print(request.args)
    sol = solve_heat_equation(request.args)
    print(len(sol[2]))
    return {
        "x": sol[0],
        "y": sol[1],
        "T": sol[2]}
