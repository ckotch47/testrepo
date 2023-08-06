
# pull the official docker image
FROM python:3.7

# set work directory
#WORKDIR /app
COPY ./.env /.env


# install dependencies
COPY ./package.txt /package.txt
RUN mkdir "uploads"
RUN pip install --no-cache-dir --upgrade -r /package.txt

COPY ./src /src

