from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)
app.debug = True

model = load("model_randomforest.pkl")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        age = float(request.form['age'])
        systolic_bp = float(request.form['systolicBP'])
        diastolic_bp = float(request.form['diastolicBP'])
        blood_sugar = float(request.form['bs'])
        body_temp = float(request.form['bodyTemp'])
        heart_rate = float(request.form['heartRate'])

        prediction = model.predict([[age, systolic_bp, diastolic_bp, blood_sugar, body_temp, heart_rate]])

        if prediction == 'high risk':
            result = 'Patient is at High Risk'
        elif prediction == 'mid risk':
            result = 'Patient is at Mid Risk'
        else:
            result = 'Patient is at Low Risk'

        return render_template('submit.html', prediction_text=result, prediction=prediction)

    return render_template('index.html')



if __name__ == '__main__':
    app.run()
