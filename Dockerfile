FROM python:3.8-slim-buster

RUN pip install requests

COPY fetch_data.py /fetch_data.py

ENTRYPOINT ["python", "/fetch_data.py"]
