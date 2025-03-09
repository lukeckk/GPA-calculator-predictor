from flask import Flask, render_template, request, redirect, url_for, session
from backend.calculator import calculate  
from backend.predictor import predict_gpa  
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = "0000"  

@app.route("/", methods=["GET", "POST"])
def home():
    calculated_result = session.get("calculated_result", None)
    predicted_result = session.get("predicted_result", None)

    session.pop("calculated_result", None)
    session.pop("predicted_result", None)

    return render_template("index.html", calculated_result=calculated_result, predicted_result=predicted_result)

@app.route("/calculate", methods=["POST"])
def calculate_gpa():
    try:
        total_credit = float(request.form["totalCredits"])
        current_credit = float(request.form["completedCredits"])
        current_gpa = float(request.form["currentGPA"])
        target_gpa = float(request.form["targetGPA"])

        session["calculated_result"] = calculate(total_credit, current_credit, target_gpa, current_gpa)

    except ValueError:
        session["calculated_result"] = "Error: Invalid input."

    return redirect(url_for("home"))

@app.route("/predict", methods=["POST"])
def predict():
    try:
        study_hours = float(request.form["studyHours"])
        work_hours = float(request.form["workHours"])
        sleep_hours = float(request.form["sleepHours"])
        interest = float(request.form["interest"])

        session["predicted_result"] = predict_gpa(study_hours, work_hours, sleep_hours, interest)

    except ValueError:
        session["predicted_result"] = "Error: Invalid input."

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
