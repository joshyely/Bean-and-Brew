FROM python:3.10

WORKDIR /src/
COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONPATH=/src

COPY ./app /src/app

CMD fastapi run app/main.py