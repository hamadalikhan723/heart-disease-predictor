from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_input = np.array([features])
        prediction = model.predict(final_input)[0]
        result = 'Heart Disease Detected' if prediction == 1 else 'No Heart Disease'
        return render_template('result.html', prediction=result)
    except:
        return "Invalid input. Please enter all 13 numerical values correctly."

if __name__ == '__main__':
    app.run(debug=True)
