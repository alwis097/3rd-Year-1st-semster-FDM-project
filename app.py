import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
import rule as r
from werkzeug.datastructures import MultiDict
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/market')
def market():
    return render_template('root.html')

@app.route('/hotel')
def hotel():
    return render_template('index.html')

@app.route('/others',methods=['POST'])
def others():
    if request.method == 'POST':
        frequent_list = request.form
        a = MultiDict(frequent_list)
        b=a.getlist('key')
        
        #key, value = list(frequent_list.items())[0]
        # value
        str1 = ','.join(b)

        print(str1)
        f_list = r.finder(str1)
        output1 = "Selected Item(s) :"+str1
        # output2 = "Frequent Item(s) :"+f_list
        
        

        return render_template('root.html', selected =output1,list_text=f_list) 

## prediction function
def ValuePredictor(predict_list):
    
    to_predict = np.array(predict_list).reshape(1, 16)
    loaded_model = pickle.load(open("XGBoost_model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        predict_list = request.form.to_dict()
        predict_list = list(predict_list.values())
        predict_list = list(map(float, predict_list))
        prediction = ValuePredictor(predict_list)
    
        if prediction == 0:
            prediction ='Hotel Booking will not be Cancelled'
        elif prediction == 1:
            prediction ='Hotel Booking can be Cancelled' 

        return render_template('index.html', prediction_text=prediction)        


if __name__ == "__main__":
    app.run(debug=True)

