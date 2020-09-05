FROM python:3.8

ADD ./fox_facts /app/fox_facts
COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

CMD [ "python", "/app/fox_facts/api.py" ]
