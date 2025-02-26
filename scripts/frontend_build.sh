#! /usr/bin/bash

running_container=beanandbrew-frontend-1
container=frontend

if [[ $(docker ps) =~ $running_container ]]
then
    echo stopping $running_container..
    docker stop $running_container
    echo removing $running_container..
    docker rm $running_container
fi

docker compose up $container -d