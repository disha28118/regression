# train_model.py - Training the regression model and saving it

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def train_and_save_model():
    # Load dataset
    df = pd.read_csv("data/house_prices.csv")
    X = df[['Bedrooms', 'Bathrooms', 'Area', 'Age']]
    y = df['Price']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model trained. MSE: {mse:.2f}")

    # Save model
    joblib.dump(model, "model/house_price_model.pkl")