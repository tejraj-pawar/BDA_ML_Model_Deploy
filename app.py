import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('linear_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html') #render_template is to redirect to index.html

@app.route('/predict_magnitude',methods=['POST'])
def predict_magnitude():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Earthquake Magnitude would be {}'.format(output))
	# above prediction_text will be replaced with "Earthquake Magnitude would be.." part. where prediction_text is place holder in index.html

# It will take latitude, longitude and depth as a query params. TODO
@app.route('/predict_magnitude_api/',methods=['GET'])
def predict_magnitude_api():
    '''
    For direct API calls through JSON request
    '''
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    depth = request.args.get('depth')
    print(latitude, longitude, depth)
    #data = request.get_json(force=True)
    prediction = model.predict([np.array([float(longitude), float(latitude), float(depth)])])

    output = round(prediction[0], 2)
    
    response = {}
    response["magnitude"] = output
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)