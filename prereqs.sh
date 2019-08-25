#/bin/bash

debian_pip_check() {
  pip -h > /dev/null
  if [ $? -ne 0 ]; then
    echo "pip is missing...installing..."
    sudo apt update && sudo apt install -y python-pip
  fi
}

debian_docker_check() {
  docker ps > /dev/null
  if [ $? -ne 0 ]; then
    echo "Docker is missing...installing..."
    sudo apt update && sudo apt install -y docker.io
  fi
}

debian_virtualenv_check() {
  virtualenv -h > /dev/null
  if [ $? -ne 0 ]; then
    echo "virtualenv is missing...installing..."
    sudo apt update && sudo apt install -y virtualenv
  fi
}

rhel_pip_check() {
  pip -h > /dev/null
  if [ $? -ne 0 ]; then
    echo "pip is missing...installing..."
    sudo yum install -y python2-pip
  fi
}

rhel_docker_check() {
  docker ps > /dev/null
  if [ $? -ne 0 ]; then
    echo "Docker is missing...installing..."
    sudo yum install -y docker
    sudo systemctl enable docker
    sudo systemctl start docker
  fi
}

rhel_virtualenv_check() {
  virtualenv -h > /dev/null
  if [ $? -ne 0 ]; then
    echo "virtualenv is missing...installing..."
    sudo yum install -y python-virtualenv
  fi
}

if [ -f /etc/redhat-release ]; then
  echo "This is a RHEL based system"
  rhel_pip_check
  rhel_docker_check
  rhel_virtualenv_check
fi

if [ -f /etc/lsb-release ]; then
  echo "This is a Debian based system"
  debian_pip_check
  debian_docker_check
  debian_virtualenv_check
fi
