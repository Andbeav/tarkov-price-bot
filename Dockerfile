FROM python:alpine3.20

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "-u", "bot.py" ]