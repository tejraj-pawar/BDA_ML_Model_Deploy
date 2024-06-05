# syntax=docker/dockerfile:1

FROM python:3.9-slim-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY templates/index.html templates/index.html
COPY app.py app.py
COPY linear_model.pkl linear_model.pkl

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]