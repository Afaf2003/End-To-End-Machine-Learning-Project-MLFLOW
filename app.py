from flask import Flask, request, render_template
from src.mlProject.pipeline.prediction import PredictionPipeline
import os
import numpy as np

application = Flask(__name__)

app = application


@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')


@app.route('/train', methods=['GET'])
def training():
    try:
        os.system("python main.py")
        return "Training Successfull!"
    except Exception as e:
        raise e
    


@app.route('/predict', methods=['POST', 'GET'])
def predictRoute():
    try:
        if request.method == 'POST':
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
            
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1,-1)
            
            obj = PredictionPipeline()
            y_pred = obj.predict(data)

            return render_template('results.html', prediction = str(y_pred))
        else:
            return render_template('index.html')
    except Exception as e:
        raise e
    


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)



