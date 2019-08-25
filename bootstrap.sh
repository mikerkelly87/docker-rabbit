#!/bin/bash

pip -h > /dev/null
if [ $? -ne 0 ]; then
    echo "Install pip prior to running this script"
    echo "ie: apt install python-pip"
    exit 1
fi

docker ps > /dev/null
if [ $? -ne 0 ]; then
    echo "Install docker prior to running this script"
    echo "ie: apt install docker.io"
    exit 1
fi

pip install ansible
