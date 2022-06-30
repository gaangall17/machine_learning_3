import joblib
import numpy as np

from flask import Flask
from flask import jsonify

app = Flask(__name__)

X_test = np.array([7.427425841,7.326573869,1.503944635,1.428939223,0.810696125,0.585384488,0.47048983,0.282661825,2.294804096])

@app.route('/predict', methods=['GET'])
def predict():
    prediction = model.predict(X_test.reshape(1, -1))
    return jsonify({'prediction': list(prediction)})


if __name__ == "__main__":
    model = joblib.load('./ml_pro/models/best_model.pkl')
    app.run(port=8080)