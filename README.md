🏠 Real Estate Price Prediction using Machine Learning
A full-stack web application built using Django, Machine Learning, and SQLite to predict real estate property prices and classify properties based on user inputs.

🚀 Features
User Registration and Login

Admin Panel for User Management

Real Estate Price Prediction using ML models (Linear Regression, Random Forest, SVM)

Property Classification based on predicted prices

Data Visualization for model performance (scatter plots, residual plots)

Secure Authentication with separate admin and user workflows

Dynamic Frontend UI with responsive design

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript (Django Templates)

Backend: Django (Python)

Database: SQLite

Machine Learning Libraries: Scikit-learn, Pandas, NumPy, Matplotlib

Deployment: Localhost (can be deployed on Heroku, Render, etc.)

📂 Project Structure
bash
Copy
Edit
final_proj/
├── admins/                  # Admin-related views and templates
├── users/                   # User-related views and templates
├── media/                   # Machine learning model files (.pkl)
├── static/                  # Static files (CSS, JS, Images)
├── templates/               # HTML Templates
├── db.sqlite3                # Database
├── manage.py                 # Django Project Manager
├── train.csv                 # Dataset used for training models
├── Compilation Procedure.txt # Setup Instructions
└── requirements.txt          # Python dependencies
🧠 Machine Learning Models
Linear Regression

Random Forest Regression

Support Vector Machine (SVM)

The best-performing model is automatically selected and deployed for predictions.
