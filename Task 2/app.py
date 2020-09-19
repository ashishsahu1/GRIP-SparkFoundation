from os import name
from flask import Flask,render_template
import pickle

app=Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

prediction = model.predict([[9.25]])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('index.html',out = prediction[0] )

    
if __name__=="__main__":
    app.run(debug=True)