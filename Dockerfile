FROM python:3.11-alpine

WORKDIR /app

RUN pip install flask

COPY ./ ./

CMD python app.py
