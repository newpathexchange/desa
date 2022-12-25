FROM python:3.8.15-buster

WORKDIR /app
COPY *.py k8s_probe.sh requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

ENTRYPOINT ["python", "-u", "produce_fake_data.py", "kubernetes"]
