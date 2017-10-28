FROM ubuntu:latest

# Install necessary tools
RUN  apt-get update && apt-get install -y nano wget curl dialog net-tools python python-pip python-dev

# Install python bottle
RUN pip install bottle
RUN pip install gunicorn
RUN pip install gevent
RUN pip install pymongo

EXPOSE 8080

RUN mkdir -p /app
COPY ./app /app
WORKDIR /app

CMD ["gunicorn","-b","0.0.0.0:8080","-w","3","-k","gevent","--log-file","-","--log-level","debug","--access-logfile","-","main_app:app"]
