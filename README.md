🫀 Heart Disease Prediction Web App
This is a machine learning-based web application that predicts the likelihood of heart disease based on 13 medical input features. It uses an ensemble model (Voting Classifier) trained with Scikit-learn and is deployed using Flask.

🔍 Features
Predicts heart disease (yes/no) based on patient health data

Built with a Voting Classifier using:

Logistic Regression

K-Nearest Neighbors

Naive Bayes

Decision Tree

Simple web interface for entering inputs

Built in Python using Flask, Scikit-learn, and NumPy

🧪 Input Features
Feature Name	Description
age	Age in years
sex	1 = Male, 0 = Female
cp	Chest pain type (0–3)
trestbps	Resting blood pressure
chol	Serum cholesterol (mg/dl)
fbs	Fasting blood sugar > 120 mg/dl
restecg	Resting ECG results
thalach	Maximum heart rate achieved
exang	Exercise-induced angina (1 = Yes)
oldpeak	ST depression induced by exercise
slope	Slope of the ST segment
ca	Number of major vessels (0–3)
thal	Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)

⚙️ Installation & Running Locally
bash
Copy
Edit
# Clone the repository
git clone https://github.com/hamadalikhan723/heart-disease-predictor.git
cd heart-disease-predictor

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
Then open http://127.0.0.1:5000/ in your browser.

📁 Project Structure
pgsql
Copy
Edit
heart-disease-predictor/
├── app.py
├── model.pkl
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
└── README.md
🌐 Live Demo
Coming soon — will be hosted on Replit or Render

📚 Dataset
This app is trained on a modified version of the Cleveland Heart Disease dataset.

🙋 Author
Hamad Ali Khan
BS Software Engineering, Kohat University of Science and Technology
GitHub: @hamadalikhan723

