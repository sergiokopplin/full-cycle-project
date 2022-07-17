FROM python:3.10.5-slim

# create user
RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src

CMD [ "tail", "-f", "/dev/null" ]