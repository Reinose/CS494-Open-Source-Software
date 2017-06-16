FROM python:2.7
MAINTAINER Gyeongwon Kim <sutt69@kaist.ac.kr>

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY ./app.py /app

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
