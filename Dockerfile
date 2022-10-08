FROM python:3.10-alpine

RUN mkdir /app
WORKDIR /app

COPY . .

RUN apk add build-base && pip install wheel
RUN pip install -r requirements.txt

CMD ["python", "main.py"]