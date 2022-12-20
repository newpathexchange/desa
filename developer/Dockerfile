FROM python:3.8.5-buster

WORKDIR /app
COPY . /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

ENV PYTHONBUFFERED=true
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:create_app('kubernetes')"]

