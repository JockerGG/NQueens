FROM python:3.9-slim-buster as base

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./ /app

######## DEBUG IMAGE ######## 
FROM base as debug

RUN pip install debugpy

CMD python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m flask run -h 0.0.0.0 -p 5000

######## PRODUCTION IMAGE ######## 
FROM base as prod
CMD flask run -h 0.0.0.0 -p 50000