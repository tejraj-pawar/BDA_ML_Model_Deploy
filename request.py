import requests

url = 'http://127.0.0.1:5000/predict_magnitude_api/?longitude=-151.4756&latitude=62.9447&depth=5'
r = requests.get(url)

print(r)