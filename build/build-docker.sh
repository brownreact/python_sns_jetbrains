#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Two arguments required - bitbucket user name and bitbucket password"
    exit 1
fi

docker build --no-cache -t python_sns ../. --build-arg BITBUCKET_USER=$1 --build-arg BITBUCKET_PASS=$2
