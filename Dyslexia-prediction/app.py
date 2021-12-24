from flask import Flask, render_template, request, jsonify
import model
import numpy as np
import pickle


app=Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home.html")
def a():
    return render_template("home.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/survey.html")
def survey():
    return render_template("survey.html")

@app.route("/quiz.html")
def quiz():
    return render_template("quiz.html")

@app.route("/predict.html")
def hello():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        output = round(prediction[0], 2)
        def pred():
            if output==0:
                return "You definately have Dyslexia, Consult a doctor ASAP!"
            elif output==1:
                return "You might have mild Dyslexia, Kindly consult a doctor!!!"
            else:
                return "You don't have Dyslexia!!" 
        return render_template('index.html', prediction_text=pred())

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__=="__main__":
    app.run(debug=True)
