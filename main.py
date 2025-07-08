# main.py - Entry point to run the model and make predictions

from train_model import train_and_save_model
from predict import make_prediction

if __name__ == "__main__":
    train_and_save_model()
    predicted_price = make_prediction([[3, 2, 1800, 20]])
    print(f"Predicted House Price: ${predicted_price:,.2f}")