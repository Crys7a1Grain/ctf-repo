FROM python:3.9-slim 

WORKDIR /app
COPY ./app /app 
COPY ./flag /flag 

RUN pip3 install -r requirements.txt

CMD gunicorn -w 4 --worker-class=gevent --worker-connections=1000 -b 0.0.0.0:25555 --chdir / --timeout 10 "main:app"