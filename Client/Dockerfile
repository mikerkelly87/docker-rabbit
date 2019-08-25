FROM ubuntu
MAINTAINER mikerkelly87@gmail.com

RUN apt update && \
apt install python3 python3-pip git -y && \
pip3 install pika && \
mkdir /opt/client && \
git clone https://github.com/mikerkelly87/docker-rabbit.git /opt/client/
