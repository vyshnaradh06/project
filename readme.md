# OpenShift Python Flask Project

Simple Flask application deployed on OpenShift.

## Run locally

python app.py

## Build Docker Image

docker build -t python-openshift-app .

## Deploy

oc apply -f openshift/
