from flask import Flask, request, jsonify
from joblib import load
from flask_cors import CORS, cross_origin

classifier = load('./../model/saved_models/classifier.joblib')

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET', 'POST'])
@cross_origin()

def basic():
    if request.method == 'POST':
        data = request.get_json()
        X_test = [x for x in data.values()]
        y_pred = classifier.predict([X_test])
        return jsonify({'predicted_value' : str(y_pred[0])})
    return ''

if __name__ == "__main__":
    app.run(debug = True)