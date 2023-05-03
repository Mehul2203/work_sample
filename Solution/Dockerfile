# FROM python:3.9
FROM apache/airflow:latest

RUN mkdir -p worksample/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . worksample/app/
COPY model.pkl worksample/app/

ENTRYPOINT [ "python", "worksample/app/app.py" ]


