FROM python:3.8

ADD ./fox_facts /app/fox_facts
COPY ./fox_facts/requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

CMD [ "python", "/app/fox_facts/main.py" ]
