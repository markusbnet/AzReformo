FROM tiangolo/uvicorn-gunicorn:python3.8

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./app /app
