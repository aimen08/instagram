FROM python:3.9

ADD . .

RUN pip install pyTelegramBotAPI python-dotenv loguru js2py


CMD [ "python", "./instagram.py" ]