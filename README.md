# Deploying-ML-model
In this we'll create simple ML model and deploy it using Flask api's

* First, run model.py file, which will create ML model and saved it on disk.
* Take a look at index.html file placed inside templates folder.
* Now, run app.py file and go to browser "http://127.0.0.1:5000/" and fill earthquake details and it will predict earthquake magnitude.
* There is another way also, i.e. by providing input to ML model through JSON. for this run request.py

## Containerization:
* Built Docker Image: 

docker build -t flask-docker-app .

* Run Docker Image:

docker run -d -p 5000:5000 flask-docker-app

Now, Go to browser "http://127.0.0.1:5000/" and fill earthquake details and it will predict earthquake magnitude
