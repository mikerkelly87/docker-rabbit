FROM ubuntu
MAINTAINER mikerkelly87@gmail.com

RUN apt update && \
apt install python3 python3-pip git default-libmysqlclient-dev -y && \
pip3 install pika && \
pip3 install mysql && \
pip3 install mysql-connector-python-rf && \
mkdir /opt/worker && \
git clone https://github.com/mikerkelly87/docker-rabbit.git /opt/worker/
