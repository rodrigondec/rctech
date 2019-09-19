# RC Tech Django project
Project made with Django + SQLite + BeautifulSoup for RC Tech interview

[![CircleCI](https://img.shields.io/circleci/build/github/rodrigondec/rctech)](https://circleci.com/gh/rodrigondec/rctech)
[![Codacy BadgeCode](https://api.codacy.com/project/badge/Grade/906a295ef1ba48ea83b0e7aa24db38c5)](https://www.codacy.com/manual/rodrigondec/rctech?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rodrigondec/rctech&amp;utm_campaign=Badge_Grade)
[![Codacy BadgeCoverage](https://api.codacy.com/project/badge/Coverage/906a295ef1ba48ea83b0e7aa24db38c5)](https://www.codacy.com/manual/rodrigondec/rctech?utm_source=github.com&utm_medium=referral&utm_content=rodrigondec/rctech&utm_campaign=Badge_Coverage)
[![License](https://img.shields.io/github/license/rodrigondec/rctech)](https://img.shields.io/github/license/rodrigondec/rctech)

# Install
## Docker + docker-compose
Install [docker-ce](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) from each documentation

### Setting up
On the project folder run the following commands:
1. `$ make config.env` to copy the file `.env.example` to `.env`
2. `$ make build` to build docker containers

# Running the project
Simply run the command `$ make up` and *voilà*.

This command will start 1 service on your machine:
- Django server on [http://0.0.0.0:8000](http://0.0.0.0:8000)

## Tests
On the project folder:
- run the command `$ make test` or `$ make test app=$(app_name)`. You may run the command `$ make coverage` instead.
- run the command `$ make flake8`

## Administration
Django Admin Site is enabled for the project on [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin).

The command `$ make populate.superuser` may be used to create the superuser `User(username='superuser', password='@Admin123')`.

## Populating Articles
The command `$ make populate.articles` may be used to fetch and save new articles from [https://www.tecmundo.com.br/](https://www.tecmundo.com.br/).
