import glob
import pickle

from flask import Flask, jsonify, request

model_file = glob.glob("model*.bin")[0]

dv_file = "dv.bin"

with open(dv_file, "rb") as f_in:
    dv = pickle.load(f_in)
with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)


app = Flask("predict_flask_service")


@app.route("/predict", methods=["POST"])
def predict():

    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    result = {
        "subscription_probability": float(y_pred),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
