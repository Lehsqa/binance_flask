## Intro

This repo is intended to make it easy to get started with a Flask project. If you want to use it for your own projects, I suggest cloning this repo locally rather than following the installation instructions below:

```
git clone <> <project-name>
```

## Installation (Docker)

Create a new docker container, using docker-compose file:

```sh
docker-compose up -d --build
```

## Running

Docker:

```sh
docker-compose up
```

Python on local host (inside the root of project):

```sh
flask --app flaskr run
```