FROM python:stretch
RUN apt-get update \
  && apt-get install -y --no-install-recommends graphviz \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir pyparsing pydot
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /code/backend
ADD . /code/backend/
WORKDIR /code
EXPOSE 40001
CMD gunicorn -w 1 -b 0.0.0.0:40001 --worker-tmp-dir /dev/shm --worker-class gevent backend:app