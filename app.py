import pickle
from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import sklearn
from urllib import response


app = Flask(__name__)

@app.route('/', methods=['POST'])
def getPred():

    #loading pickle model
    with open('model_pickle', 'rb') as f:
        mp = pickle.load(f)

    # getting request form data
    gender = request.form.get('gender')
    parLvl = request.form.get('parental level of education')
    race = request.form.get('race/ethnicity')
    lunch = request.form.get('lunch')
    testPrep = request.form.get('test preparation course')
    readingScore = request.form.get('reading score')
    mathScore = request.form.get('math score')

    # make prediction based on form inputs
    prediction = mp.predict([[float(gender), float(race), float(parLvl), float(lunch), float(testPrep), float(mathScore), float(readingScore)]])
    pred = str(prediction[0])

    #return prediction
    response = jsonify({'prediction': pred})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/index', methods=['POST'])
def index():
    param  = request.form.get('pr')

    response = jsonify({'some': param})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    app.run(debug=True)
