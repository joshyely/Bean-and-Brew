#! /usr/bin/bash

if [[ ! $PWD =~ "frontend" ]]
then
    cd "$PWD/frontend"
fi

npm install
npm run dev -- --port 3000