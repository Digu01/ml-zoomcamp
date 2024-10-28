#!/bin/bash

# Answer questions for homework 5
# Assumes that you have already built the python env

# Function to print a nicer header
header() {
    echo $1
    printf '=%.0s' {1..80}
    echo
}

echo "Beginning HW 5"

# Q1
header "Question 1"
version=$(pipenv --version)
echo "Running ${version}"

# Q2
header "Question 2"
hash=$(cat Pipfile.lock | jq '.default."scikit-learn".hashes[0]')
echo "The first hash for scikit-learn is ${hash}"

# Q3
header "Question 3"
echo "Running prediction job"
pipenv run python score_client.py --payload '{"job": "management", "duration": 400, "poutcome": "success"}'

# Q4
header "Question 4"
echo "Launching the gunicorn server"
pipenv run gunicorn --pid PID_FILE --bind 0.0.0.0:9696 predict_flask_service:app --daemon
echo "Running prediction job"
pipenv run python predict_score_flask.py --payload '{"job": "student", "duration": 280, "poutcome": "failure"}'
sleep 3
echo "Stopping the gunicorn server"
kill $(cat PID_FILE)

# Q5
header "Question 5"
# Lazy way
img_size=$(docker images | grep zoomcamp-model | xargs | cut -d " " -f 7)
echo "The size of the base image is ${img_size}"

# Q6
IMG_NAME="ml_hw5"
header "Question 6"
echo "Building Docker container"
docker build -q -t $IMG_NAME .
echo "Launching Docker container"
docker run -p 9696:9696 -d --name=${IMG_NAME} $IMG_NAME
container_id=$(docker ps -a -f name=${IMG_NAME} --format json | jq -r .ID)
echo "Running prediction job"
pipenv run python predict_score_flask.py --payload '{"job": "management", "duration": 400, "poutcome": "success"}'
echo "Stopping container"
docker stop $container_id > /dev/null
docker container rm $container_id > /dev/null
