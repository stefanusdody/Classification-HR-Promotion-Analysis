import numpy as np
import pickle
import flask

# Create flask app
app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template("main.html")) 

# load pickle model
model = pickle.load(open('model/model_classifier.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in flask.request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    output = {0: "Employee will not Promote", 1:"Employee will Promote"  }

    return flask.render_template("main.html", prediction_text ="Possible that the {}".format(output[prediction[0]]))

if __name__ == "__main__":
    app.run(debug=True)