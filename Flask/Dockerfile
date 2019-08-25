FROM ubuntu
MAINTAINER mikerkelly87@gmail.com

RUN apt update && \
apt install python3 python3-pip git default-libmysqlclient-dev -y && \
pip3 install Flask && \
pip3 install pymysql && \
mkdir /opt/flask && \
git clone https://github.com/mikerkelly87/docker-rabbit.git /opt/flask/
