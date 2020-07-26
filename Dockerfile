FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
RUN pip install -U setuptools

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
		gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /restaurantapp
WORKDIR /restaurantapp
COPY ./restaurantapp /restaurantapp

RUN mkdir -p /mediafiles
RUN mkdir -p /staticfiles
RUN adduser -D user
RUN chown -R user:user /staticfiles
RUN chown -R user:user /mediafiles
RUN chmod -R 755 /staticfiles
RUN chmod -R 755 /mediafiles
USER user