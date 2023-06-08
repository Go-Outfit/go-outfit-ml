FROM python:alpine3.18

RUN apk update && apk upgrade
RUN apk add --no-cache  git

WORKDIR /app

COPY . .

RUN pip3 install .

EXPOSE 8080


CMD ["python3","-m","flask","run","--host=0.0.0.0","--port=8080"]