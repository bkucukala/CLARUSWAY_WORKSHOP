FROM python:alpine
ENV GREETING="Hallo"
ENV USERNAME="Test"
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]