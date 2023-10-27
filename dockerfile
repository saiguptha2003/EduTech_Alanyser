# syntax=docker/dockerfile:1
FROM python:3.8
WORKDIR /python-docker
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]