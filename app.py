import numpy as np
from flask import Flask, request, jsonify, render_template
# import pickle
import joblib 
import pandas as pd



app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    try:
        data = request.get_json()
        passenger_class = data.get('passengerClass')
        age = data.get('age')
        embarked = data.get('embarked')
        fare = data.get('fare')
        sex = data.get('sex')
        parch = data.get('parch'),
        sibsp = data.get('sibsp')
        ##prediction stuff here
        input = pd.DataFrame(
            data=
                {
                    'Pclass':[passenger_class],
                    'Sex':[sex],
                    'Age':[age],
                    'SibSp':[sibsp],
                    'Parch':[parch][0],
                    'Fare':[fare],
                    'Embarked':[embarked],
                    


                }
    
        )
        print(input)
        prediction = model.predict(input)[0]
        print(prediction)
        #### result
        if prediction == 0:
            message = "Doesn't Survive"
        else:
            message = "Survives"
        result = {
            'message': message
        }
        return jsonify(result),200

    except Exception as e:
        print(e)
        return jsonify({'error':'An error occured'}),500
    

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
