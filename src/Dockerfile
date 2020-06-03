FROM python:3.8-slim-buster

LABEL MAINTAINER="Luiz Henrique Longo <longo.luizh@gmail.com>"

WORKDIR /app

COPY . /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]