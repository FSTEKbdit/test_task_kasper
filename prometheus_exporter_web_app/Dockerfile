FROM python:3.9.21-alpine

RUN apk update

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /opt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY prometheus_test.py .
ENTRYPOINT ["python3", "prometheus_test.py"]
