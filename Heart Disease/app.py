from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
## Load the model
try:
    with open('trained_model.sav', 'rb') as file:
        model = pickle.load(file)
except EOFError:
    print("The file is empty or does not exist. Please make sure the file exists and has data in it.")
except Exception as e:
    print(f"An error occurred: {e}")  
else:
    # code that uses the model only if it was successfully loaded
    print(model) 

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        Gender = request.form['sex']
        if (Gender == 'male'):
            Gender = 0
        else:
            Gender = 1
        currentSmoker = float(request.form['currentSmoker'])
        cigsPerDay = float(request.form['cigsPerDay'])
        BPMeds = float(request.form['BPMeds'])
        prevalentStroke = float(request.form['prevalentStroke'])
        prevalentHyp = float(request.form['prevalentHyp'])
        diabetes = float(request.form['diabetes'])
        totChol = float(request.form['totChol'])
        sysBP = float(request.form['sysBP'])
        diaBP = float(request.form['diaBP'])
        BMI = float(request.form['BMI'])
        heartRate = float(request.form['heartRate'])
        glucose = float(request.form['glucose'])
  
        values = np.array([[Gender,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose]])
        prediction = model.predict(values)
        prediction = round(prediction[0],2)
    

        return render_template('index.html', prediction_text='Heart Disease 0 means no Heart Disease. 1 is Heart Disease .Result is {}'.format(prediction))





if __name__ == "__main__":
    app.run(debug=True)