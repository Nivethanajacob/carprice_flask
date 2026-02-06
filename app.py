from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        year = int(request.form["year"])
        present_price = float(request.form["present_price"])
        kms_driven = int(request.form["kms_driven"])
        owner = int(request.form["owner"])

        fuel_type = request.form["fuel_type"]
        seller_type = request.form["seller_type"]
        transmission = request.form["transmission"]

        # Encoding (same as training)
        fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
        seller_map = {"Dealer": 0, "Individual": 1}
        transmission_map = {"Manual": 0, "Automatic": 1}

        fuel_type = fuel_map[fuel_type]
        seller_type = seller_map[seller_type]
        transmission = transmission_map[transmission]

        # Final input (ORDER MUST MATCH TRAINING DATA)
        final_features = np.array([[ 
            year,
            present_price,
            kms_driven,
            fuel_type,
            seller_type,
            transmission,
            owner
        ]])

        prediction = model.predict(final_features)[0]

        return render_template(
            "index.html",
            prediction_text=f"Estimated Car Price: ₹ {round(prediction, 2)} Lakhs"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text="Error occurred. Please check input values."
        )

if __name__ == "__main__":
    app.run(debug=True)
