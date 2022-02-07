FROM python:alpine
MAINTAINER "Clarusway DevOps Team"
ENV GREETING="Hallo"
ENV USERNAME="Test"
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]