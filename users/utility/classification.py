import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from django.shortcuts import render

from Real_Estate  import settings # Import render

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    return {"RMSE": rmse, "R2": r2, "y_pred": y_pred, "y_test": y_test}

def execute_real_estate_prediction():  # Take request as argument
    data_path = r"C:\Users\lakesh monika\Desktop\final proj\Real_Estate\media\train.csv"
    
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        return {"Error": f"CSV file not found at {data_path}"}
    
    df = df.dropna()
    X = df[['RERA', 'BHK_NO.', 'SQUARE_FT', 'READY_TO_MOVE', 'RESALE', 'LONGITUDE', 'LATITUDE']]
    y = df['TARGET(PRICE_IN_LACS)']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "SVM": SVR()
    }
    
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        results[name] = evaluate_model(model, X_test, y_test)
        
    import joblib

    # Save all models
    for model_name, model in models.items():
        joblib.dump(model, f"media/{model_name}_model.pkl")

    # Save the best model separately
    best_model_name = max(results, key=lambda x: results[x]['R2'])
    best_model = models[best_model_name]
    joblib.dump(best_model, "media/best_model.pkl")

    # Calculate and print the correlation matrix
    correlation_matrix = X.corr()

    # Generate and save plots for the best model
    y_pred = results[best_model_name]['y_pred']
    y_test = results[best_model_name]['y_test']

    # Scatter plot of predicted vs. actual values
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title(f"{best_model_name}: Actual vs. Predicted Prices")
    plt.savefig("media/scatter_plot.png")
    plt.close()

    # Histogram of residuals (prediction errors)
    residuals = y_test - y_pred
    plt.figure(figsize=(8, 6))
    sns.histplot(residuals, kde=True)
    plt.xlabel("Residuals")
    plt.title(f"{best_model_name}: Residual Distribution")
    plt.savefig("media/residual_plot.png")
    plt.close()

    # Prepare data to be sent to the template
    context = {
        "results": results,
        "best_model_name": best_model_name,
        "correlation_matrix": correlation_matrix.to_html(),
        "scatter_plot_url": "media/scatter_plot.png",
        "residual_plot_url": "media/residual_plot.png",
        "saved_models": [f"{name}_model.pkl" for name in models.keys()]
    }

    return context


def predict_price(rera, bhk_no, square_ft, ready_to_move, resale, longitude, latitude,model):
    """Predicts the price using the best model."""
    input_data = np.array([[rera, bhk_no, square_ft, ready_to_move, resale, longitude, latitude]])

    try:
        if model==0:

            model_path = r"media/best_model.pkl"
            model = joblib.load(model_path)
            return model.predict(input_data)[0]
        elif model==1:

            model_path =  r"media/Linear Regression_model.pkl"
            model = joblib.load(model_path)
            return model.predict(input_data)[0]
        elif model==2:

            model_path =  r"media/Random Forest_model.pkl"
            model = joblib.load(model_path)
            return model.predict(input_data)[0]
        elif model==3:

            model_path =  r"media/SVM_model.pkl"
            model = joblib.load(model_path)
            return model.predict(input_data)[0]
        
    except FileNotFoundError:
        return "Error: Model file not found. Please ensure the models are trained and saved correctly."
    except Exception as e:
        return f"An error occurred during prediction: {e}"
    
