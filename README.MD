# Deployment  
Create the Directory for the repo  
`mkdir ~/docker-rabbit`  
  
Clone the repo  
`git clone https://git.mikerkelly.com/mikerkelly87/python-rabbit.git ~/docker-rabbit`  
  
Go into the repo directory  
`cd ~/docker-rabbit/`  
  
Install Required Software  
`bash ./prereqs.sh`  
  
Create the Virtual Environment  
`virtualenv ansible_venv`
  
Activate the Ansible Virtual Environment  
`source ansible_venv/bin/activate`  
  
Bootstrap Ansible  
`bash ./bootstrap.sh`  
  
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
`docker exec -it worker /opt/worker/worker.py`  
  
After you send the message you can verify it was inserted into the database  
by connecting to `http://<DOCKER_HOST_IP>:5000`  
Be sure that port 5000 is open on the Docker host before attempting this.  
  
Alternatively you can verify it was inserted into the database  
by the worker by first connecting to the mariadb container  
`docker exec -it mariadb /bin/bash`  
  
Once inside the container you can query the database table  
`mysql -e "SELECT * FROM rabbitmq.messages;"`  
