FROM python:2.7-alpine

ENV PYTHONUNBUFFERED=1

ARG BITBUCKET_USER
ARG BITBUCKET_PASS

RUN apk add --no-cache \
    git \
    gcc \
    musl-dev

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN sed -i "s/auth = ''/auth = '$BITBUCKET_USER:$BITBUCKET_PASS@'/" /usr/src/app/setup.py && \
    pip install -U setuptools && \
    pip install -U pylint && \
    python setup.py install --user

ENTRYPOINT ["/usr/src/app/build/docker-entrypoint.sh"]
