#! /usr/bin/bash
run() {
    npm install
    npm run dev -- --port 3000
}


if [[ ! $PWD =~ "frontend" ]]
then
    cd "$PWD/frontend"
    run
    cd ..
else
    run
fi

