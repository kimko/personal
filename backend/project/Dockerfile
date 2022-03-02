FROM python:3.10.1-slim-buster

# working directory
WORKDIR /usr/src/app

# prevent writing pyc files to disc 
ENV PYTHONDONTWRITEBYTECODE 1
# dont buff stdout and stderr 
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements .
RUN pip install -r requirements

COPY . .
COPY ./entrypoint.sh .

RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
