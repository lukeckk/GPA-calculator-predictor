from flask import Flask, render_template, request
from backend.backend import calculate  
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route("/", methods=["GET", "POST"])
def home():
    result = None  # Default value
    if request.method == "POST":
        try:
            total_credit = float(request.form["totalCredits"])
            current_credit = float(request.form["completedCredits"])
            current_gpa = float(request.form["currentGPA"])
            target_gpa = float(request.form["targetGPA"])

            result = calculate(total_credit, current_credit, target_gpa, current_gpa)

        except ValueError:
            result = "Error: Invalid input."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
