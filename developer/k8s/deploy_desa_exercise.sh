#!/bin/bash

kubectl apply -f desa-exercise-cfgmap.yaml
kubectl apply -f desa-exercise-deployment.yaml
kubectl apply -f desa-exercise-service.yaml
#kubectl apply -f oikos-ingress.yaml

