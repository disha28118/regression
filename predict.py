# predict.py - Make predictions using the trained model

import joblib

def make_prediction(features):
    model = joblib.load("model/house_price_model.pkl")
    return model.predict(features)[0]