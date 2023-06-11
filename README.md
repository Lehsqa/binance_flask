## Intro

This repo is intended to make it easy to get started with a Flask project. If you want to use it for your own projects, I suggest cloning this repo locally rather than following the installation instructions below:

```
git clone https://github.com/Lehsqa/binance_flask.git <project-name>
```

After cloning the repo need to configure config.py file (https://www.binance.com/en/my/settings/api-management)

```
API_KEY = <API Key>
SECRET_KEY = <Secret Key>
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