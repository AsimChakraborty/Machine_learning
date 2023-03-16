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
        time = float(request.form['time'])
        V1 = float(request.form['V1'])
        V2 = float(request.form['V2'])
        V3 = float(request.form['V3'])
        V4 = float(request.form['V4'])
        V5 = float(request.form['V5'])
        V6 = float(request.form['V6'])
        V7 = float(request.form['V7'])
        V8 = float(request.form['V8'])
        V9 = float(request.form['V9'])
        V10 = float(request.form['V10'])
        V11 = float(request.form['V11'])
        V12 = float(request.form['V12'])
        V13 = float(request.form['V13'])
        V14 = float(request.form['V14'])
        V15 = float(request.form['V15'])
        V16 = float(request.form['V16'])
        V17 = float(request.form['V17'])
        V18 = float(request.form['V18'])
        V19 = float(request.form['V19'])
        V20 = float(request.form['V20'])
        V21 = float(request.form['V21'])
        V22 = float(request.form['V22'])
        V23 = float(request.form['V23'])
        V24 = float(request.form['V24'])
        V25 = float(request.form['V25'])
        V26 = float(request.form['V26'])
        V27 = float(request.form['V27'])
        V28 = float(request.form['V28'])
        Amount = float(request.form['Amount'])
  
        values = np.array([[time, V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])
        prediction = model.predict(values)
        prediction = round(prediction[0],2)
        if (prediction == 0):
            prediction_text = 'Your Credit Card legit'
        else:
            prediction_text = 'Your Credit Card Fraud'
       
        return render_template('dashboard.html', prediction_text=prediction_text)    


@app.route('/dashboard',methods=['GET','POST']) 

def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)