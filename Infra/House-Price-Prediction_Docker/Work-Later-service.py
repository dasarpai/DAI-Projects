#If some api request is coming to this server then how this service will respond will be implemented here.

import os
from flask import Flask, jsonify, request
import pickle

#import json
col_imp = ["grade", "lat", "long", "sqft_living", "waterfront", "yr_built"]

model_houseprice = pickle.load(open('model_houseprice.pkl', 'rb'))
def predict(dict_values, col_imp=col_imp, clf=model_houseprice):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = model_reg.predict(x)[0]
    return y_pred


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def flask_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def server_is_up():
        return 'server is up'

    @app.route('/predict_price', methods=['POST'])
    def start():
        to_predict = request.json

        print("I am here",to_predict)
        pred = predict(to_predict)
        pred=1000098
        return jsonify({"predict cost":pred})

    @app.route('/results',methods=['POST'])
    def results():
        data = request.get_json(force=True)
        prediction = model.predict([np.array(list(data.values()))])
        output = prediction[0]
        return jsonify(output)

    return app

if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True)
    #app.run(debug=True, host='0.0.0.0')