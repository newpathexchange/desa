# Developer Exercise

REST API built in Python Flask, with flask-smorest
  * uses Marshmallow for API schemas (serialize/deserialize and format checks)
  * implements OpenAPI with API browsing and generation of api-spec.json
  * Kubernetes deployment, service, and cfgmap
    * uses port 30080 instead of 8080
    * this is more simple to avoid ingress controller, load balancer, and DNS setup

Kubernetes setup
```
./docker_build.sh v0.1.2
cd k8s
./deploy_desa_exercise.sh
```

Unit test execution
```
. ~/.venv/desa-dev/bin/activate
python -m pytest
```

Example cURL commands for testing
```
# get
curl http://kube-worker1.lab.newpathexchange.com:30080/api/hello
curl "http://kube-worker1.lab.newpathexchange.com:30080/api/add?num1=3.5&num2=4.6"
curl "http://kube-worker1.lab.newpathexchange.com:30080/api/time?days=45"
curl "http://kube-worker1.lab.newpathexchange.com:30080/api/weather?uszip=21207"
# post
curl -H "Content-type: application/json" -d '{"num1": 3.5, "num2": 4.6}' http://kube-worker1.lab.newpathexchange.com:30080/api/add
curl -H "Content-type: application/json" -d '{"days": 45}' http://kube-worker1.lab.newpathexchange.com:30080/api/time
curl -H "Content-type: application/json" -d '{"uszip": "21207"}' http://kube-worker1.lab.newpathexchange.com:30080/api/weather

```
