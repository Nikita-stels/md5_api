FROM python:3.6
COPY . /code
WORKDIR /code
ENV FLASK_CONFIG config.py
RUN pip install -r md5_api/requirements.txt
