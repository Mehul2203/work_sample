from __future__ import division, print_function
import numpy as np
import joblib


# Flask utils
from flask import Flask, redirect, url_for, request, render_template

# Load the model from the file


# Define a flask app
app = Flask(__name__)
model = joblib.load('worksample/app/model.pkl')

@app.route('/')
def home():
    return "Welcome to Model Deployment!!"


@app.route('/predict')
def predict():
    # Get values from browser
    vol_moving_avg = request.args['vol_moving_avg']
    adj_close_rolling_med = request.args['adj_close_rolling_med']

    test_inp = np.array([vol_moving_avg, adj_close_rolling_med]).reshape(1, 2)
    volume_predicted = model.predict(test_inp)[0]
    output = "Predicted Volume: " + str(volume_predicted)

    return (output)


if __name__ == '__main__':
    print("Running Application on local host with port 5000")
    app.run(host='localhost', debug=True, port=5000)
    print("Application started")



