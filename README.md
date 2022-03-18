# Convert numbers from roman to arabic and vice versa

## Requirements

* Docker 20.10
* Docker-compose 1.25


## Setup & build
* Create a .env file using .env.example
  * You could provide `$PORT` to .env to run web on it (8000 by default)
* Run docker build:  
  * `docker-compose build`
* In addition - install poetry dependencies:
    * pip install poetry
    * poetry install


## Runing the application
* Run with docker:
  * `docker-compose up`
* Run locally:
    * `poetry run python manage.py migrate`
    * `poetry run python manage.py runserver`


Default application url: ` 127.0.0.1:8000 `

## Production

You can check the production for this app at `https://roman-arabic-converter.herokuapp.com/`
