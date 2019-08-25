FROM mariadb:latest
MAINTAINER mikerkelly87@gmail.com

ENV MYSQL_ROOT_PASSWORD=S3cur3

RUN apt update && apt install git -y && \
mkdir /root/docker-rabbit && \
git clone https://github.com/mikerkelly87/docker-rabbit.git /root/docker-rabbit/ && \
echo "bind-address=0.0.0.0" >> /etc/mysql/my.cnf && \
echo "[client]" > /root/.my.cnf && \
echo "user=root" >> /root/.my.cnf && \
echo "password=S3cur3" >> /root/.my.cnf
