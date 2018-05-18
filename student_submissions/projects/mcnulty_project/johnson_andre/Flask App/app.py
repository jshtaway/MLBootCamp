from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import jsonify
from sklearn.externals import joblib
import pandas as pd
import numpy as np
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template(
        'home.html')
 
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html',name=name)

@app.route('/predict')
def predict():
	return render_template('predict_form.html')

@app.route('/d3')	
def d3():
	return render_template('d3.html')

	
@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		# print(result['Customer_Data'])
		# json_ = result.json
		# query_df = pd.DataFrame(result)
		result1 = result['Customer_Data'].split(',')
		# result2 = map(float, result1)
		result2 = np.array(result1).reshape(1,-1)
		result_np = result2.astype(float)
		
		# print(result_np)
		# print(result_np.shape)
			   
			   
		prediction = lr_model.predict(result_np)
		# print(prediction)
		# prediction = jsonify({'prediction': list(prediction)})
		return render_template("result.html",result = prediction)
 
if __name__ == "__main__":
	lr_model = joblib.load('lr_model.pkl')
	model_columns = joblib.load('lr_model_columns.pkl')
	app.run(host='0.0.0.0', port=8080)