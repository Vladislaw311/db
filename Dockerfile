FROM python:3.10

WORKDIR /app

COPY ./bd-main ./

COPY ./bd.txt ./

RUN pip install -q pymysql -r bd.txt

COPY ./ /app/ 

EXPOSE 80

CMD ["python","main.py"]