FROM python:3.12
ENV PYTHONUNBUFFERED 1
RUN mkdir /fc_clubs
WORKDIR /fc_clubs
ADD . /fc_clubs
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install mysqlclient
COPY . /fc_clubs

#ENTRYPOINT ["./docker/entrypoint.sh"]