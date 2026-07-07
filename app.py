from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    income = request.form['income']
    children = request.form['children']
    family = request.form['family']
    gender = request.form['gender']
    car = request.form['car']
    house = request.form['house']

    # ----------------------------------------------------
    # Temporary Prediction Logic
    # (Will be replaced with ML model later)
    # ----------------------------------------------------

    if int(income) >= 100000:
        prediction = "Credit Card Approved"
    else:
        prediction = "Credit Card Rejected"

    return f"<h2>{prediction}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
