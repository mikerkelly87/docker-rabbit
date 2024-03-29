# Design  
![Image description](figures/docker-rabbit.png)  
  
# Notes  
At this point in time this has only been tested on `CentOS 7`, `Ubuntu 16.04`, and `Ubuntu 18.04`.  
It also requires you to run all of this as the `root` user.  

# Deployment  
Create the Directory for the repo  
```
mkdir ~/docker-rabbit
```
  
Clone the repo  
```
git clone https://github.com/mikerkelly87/docker-rabbit.git ~/docker-rabbit
```
  
Go into the repo directory  
```
cd ~/docker-rabbit/
```
  
Install Required Software  
```
bash ./prereqs.sh
```
  
Create the Virtual Environment  
```
virtualenv ansible_venv
```
  
Activate the Ansible Virtual Environment  
```
source ansible_venv/bin/activate
```
  
Bootstrap Ansible  
```
bash ./bootstrap.sh
```
  
Run the Ansible playbooks  
```
ansible-playbook ~/docker-rabbit/playbooks/main.yml --skip-tags "db_create"  
ansible-playbook ~/docker-rabbit/playbooks/main.yml --tags "db_create"
```
  
# Usage  
This setup will send a message to a RabbitMQ message queue  
After the message is sent the worker container will retrieve the message  
and insert it into the `rabbitmq` database on the mariadb container  
  
Send a message  
```
docker exec -it client /opt/client/client.py
```
  
After you send the message you can verify it was inserted into the database  
by connecting to:  
```
http://<DOCKER_HOST_IP>:5000
```
Be sure that port 5000 is open on the Docker host before attempting this.  
  
Alternatively you can verify it was inserted into the database  
by the worker by first connecting to the mariadb container  
```
docker exec -it mariadb /bin/bash
```
  
Once inside the container you can query the database table  
```
mysql -e "SELECT * FROM rabbitmq.messages;"
```
