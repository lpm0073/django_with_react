# Hybrid Django + ReactJS Reference Project
[![hack.d Lawrence McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)
[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

License: MIT

This is a fully functional reference project that demonstrates a hybrid Django + ReactJS setup. After building this environment locally you can view [this example page](http://localhost:8000/app) with ReactJS running inside of Django. 

The React app in this project was scaffolded with [Create React App](https://create-react-app.dev/). It is completely scalable and is wrapped inside of a Django app located in [django_with_react/djangoapps/frontend](https://github.com/lpm0073/django_with_react/tree/main/django_with_react/djangoapps/frontend). You build the React app normally, using `npm run build` or `yarn run build`. This [single view](https://github.com/lpm0073/django_with_react/blob/main/django_with_react/djangoapps/frontend/views.py) within the frontend app enables the Django templating system to automatically find and seamlessly integrate the React build's optimized js and css bundles. You have the option of using both Django urls.py as well as React Router. Additionally, you can pass data to the React app using both a traditional REST api or using the Django template context. The React build is served entirely by Django's templating system and native static asset functionality.

There are some anciliary objectives as well that bear mentioning. The local development stack consists of the following fundamental building blocks:

1. **Python Virtual Environment** This project uses Python3.9 with what I consider to be the ideal set of PyPi packages for a garden variety Django project as of this writing.
2. **Django** project that was scaffolded with [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) and includes a fully configured implementation of [Django REST Framework](https://www.django-rest-framework.org/) that is ideally suited for serving a REST api for the ReactJS frontend.
3. The **ReactJS** app.
4. **Sphinx** documentation server that was also scaffolded with CookieCutter
5. **Docker** which provides all backend services (see the list below, in this section)
6. **HTTPS**. This project also includes documentation and an example of how to implement https in your local development environment, which is helpful for things like testing oauth.
7. **Opinionated Code Styling Enforcement**. This project includes an example implementation of `pre-commit` with `black` and `flake8` code formatters.

The Docker backend services consist of the following:
 -  Django WSGI app server:
    - http://localhost:8000
    - https://django_with_react.stepwisemath.local/
 - Nginx server
 - Postgres database server: port 5432
 - Sphinx Documentation server: http://localhost:7000
 - Flower server: http://localhost:5555
 - Celery worker
 - CeleryBeat server

## Quick Start

Development environment prerequisites:
- Docker 20.x.x
- Python 3.9
- node 14.x.x
- npm 8.x.x


### 1. clone this repo
```bash
git clone https://github.com/lpm0073/django_with_react.git
cd django_with_react
```

### 2. Python Django Initializations
```bash
python -m venv venv
source .envs/.local/.django     # environment variables for Django as well as Docker
source .envs/.local/.postgres   # PostgreSQL host, db, user, pwd
source venv/bin/activate        # the Python virtual environment, for VS Code linting and auto code completion
pip install -r requirements/local.txt
```

### 3. ReactJS Initialization
```bash
cd ./django_with_react/djangoapps/frontend/
npm install
cd ../../../
```

### 4. Launch Docker
```bash
docker-compose -f local.yml up --build
```

### 5. Initialize Postgres
```bash
sudo rm -r ./db/
mkdir ./db
mkdir ./db/data/
mkdir ./db/backups/
initdb ./db/data/
```

### 6. View the app
http://localhost:8000/app


## Better, Smarter Start

This repo is only intended to serve as a reference. You really should build your own environment, using this project as a guide.

### Cookie Cutter Django Settings

Following are my responses to the Cookie Cutter Django on-screen questionnaire.

```bash
cookiecutter https://github.com/cookiecutter/cookiecutter-django

$ project_slug [django_with_react]: 
$ description [Behold My Awesome Project!]: Hybrid Django + ReactJS setup   
$ author_name [Daniel Roy Greenfeld]: Lawrence McDaniel
$ domain_name [example.com]: dwr.lawrencemcdaniel.com    
$ email [lawrence-mcdaniel@example.com]: lpm0073@gmail.com
$ version [0.1.0]: 
$ Select open_source_license: 
1 - MIT
2 - BSD
3 - GPLv3
4 - Apache Software License 2.0
5 - Not open source
$ Choose from 1, 2, 3, 4, 5 [1]: 1

$ timezone [UTC]: 
$ windows [n]: n
$ use_pycharm [n]: n
$ use_docker [n]: y
$ Select postgresql_version:
1 - 14.1
2 - 13.5
3 - 12.9
4 - 11.14
5 - 10.19
$ Choose from 1, 2, 3, 4, 5 [1]: 

$ Select js_task_runner:
1 - None
2 - Gulp
$ Choose from 1, 2 [1]: 

$ Select cloud_provider:
1 - AWS
2 - GCP
3 - None
$ Choose from 1, 2, 3 [1]: 

$ Select mail_service:
1 - Mailgun
2 - Amazon SES
3 - Mailjet
4 - Mandrill
5 - Postmark
6 - Sendgrid
7 - SendinBlue
8 - SparkPost
9 - Other SMTP
$ Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9 [1]: 2

$ use_async [n]: y
$ use_drf [n]: y
$ custom_bootstrap_compilation [n]: n
$ use_compressor [n]: y
$ use_celery [n]: y
$ use_mailhog [n]: n
$ use_sentry [n]: y
$ use_whitenoise [n]: y
$ use_heroku [n]: n
$ Select ci_tool:
1 - None
2 - Travis
3 - Gitlab
4 - Github
$ Choose from 1, 2, 3, 4 [1]: 4

$ keep_local_envs_in_vcs [y]: y
$ debug [n]: n
```

### Setting up your local dev environment

1. **Run cookiecutter-django**

2. **Create a virtual environment** We're using Python 3.9x for this project. On macOS Homebrew is the best way to install specific versions of Python. Note that by using Homebrew you'll be able to safely install multiple versions of Python.


```bash
# check your python version
python3.9 --version

cd github/querium/stepwisemath.ai/django_with_react/
python3.9 -m venv venv
```

3. **Launch the virtual environment**

```bash
cd github/querium/stepwisemath.ai/django_with_react/
source .envs/.local/.django     # environment variables for Django as well as Docker
source .envs/.local/.postgres   # PostgreSQL host, db, user, pwd
source venv/bin/activate        # the Python virtual environment, for VS Code linting and auto code completion
```

4. **Launch Docker Desktop** or a docker daemon

5. **Build and launch the docker image** This will launch all backend services simultaneously, noting that these will be running from within the Docker container rather than your macOS environment. Therefore, for any of these services to be exposed outside of the Docker container they have to be explicitly mounted.

```bash
cd github/querium/stepwisemath.ai/django_with_react/
docker-compose -f local.yml build
docker-compose -f local.yml up
```

### Setting up HTTPS on local dev environment

See:
- [Developing locally with HTTPS](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html?highlight=https#developing-locally-with-https)

- [MKCERT: VALID HTTPS CERTIFICATES FOR LOCALHOST](https://words.filippo.io/mkcert-valid-https-certificates-for-localhost/)

```bash
# edit your hosts file
vim /etc/hosts

# add this near the bottom of the file
127.0.0.1 django_with_react.local

# you'll need to restart your local computer afterwards.
```

Test your connection: https://django_with_react.local/

### Setting up Postgres in your local Dev environment

See this article on locally [setting up Postrgres with Docker:](https://betterprogramming.pub/how-to-run-postgresql-in-a-docker-container-on-macos-with-persistent-local-data-440e7172821e)

```bash
# from inside your project root folder. ie django_with_react/
mkdir ./db
mkdir ./db/data/
mkdir ./db/backups/
initdb ./db/data/
```

### Docker Guide

This project relies on Docker for both the development environment in macOS as well as the deployment enivronment on AWS EC2 Ubuntu 20.04 LTS.

Note the two yaml files in the root of this project, `./local.yml` and `./production.yml` containing the Docker image build specifications for all of the backend services described above.

- See detailed [cookiecutter-django Docker Development documentation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html).

- Also see: https://docs.docker.com/samples/django/

```bash
# Build and launch the docker containers
docker-compose -f local.yml up --build

# Run docker containers as a daemon
docker-compose -f local.yml up -d

# View docker container states
docker-compose -f local.yml ps

# View logs
docker-compose -f local.yml logs

# command line syntax guideline
docker-compose -f local.yml run --rm [SERVICE] [service-specific command]
# where [SERVICE] is one of: django, postgres, redis, node, flower, docs, celeryworker, celerybeat

# Example Django commands
docker-compose -f local.yml run --rm django python manage.py collectstatic
docker-compose -f local.yml run --rm django python manage.py startapp
docker-compose -f local.yml run --rm django python manage.py migrate
docker-compose -f local.yml run --rm django python manage.py createsuperuser
docker-compose -f local.yml run --rm django python manage.py shell
docker-compose -f local.yml run --rm django python manage.py test

# Example Postgres commands
docker-compose -f local.yml run --rm postgres psql -d django_with_react -U vyLNQFrxbTPUWjLCLMndHtYfbmrKsNYV -W
# pwd: JVUYsywPXB3uHJocoC19mkRacYlZqR8EFNl5qjYthlkNiml4owZXfR1corVm3aAO
```

#### Trouble shooting Docker

On macOS: AirPlay Receiver listens on port 7000, which conflicts with the Sphinx Documentation
docker container `django_with_react_local_docs` described in local.yml.

See: https://developer.apple.com/forums/thread/682332

To resolve: disable `Airplay Receiver` in `System Prferences` / `Sharing`. Then verify that the port is available with the following

```bash
# Error response from daemon: Ports are not available: listen tcp 0.0.0.0:7000: bind: address already in use
sudo lsof -i tcp:7000
```

### Setting Up and Integrating ReactJS


#### Django app
```bash
# scaffold a new djangoapp
mkdir ./django_with_react/djangoapps
docker-compose -f local.yml run --rm django python manage.py startapp frontend
mv ./frontend ./django_with_react/djangoapps/

cd ./django_with_react/djangoapps/frontend
node --version
npm --version
npx --version
```

#### ReactJS

see: [Create a New React App](https://reactjs.org/docs/create-a-new-react-app.html)

```bash
cd ./django_with_react/djangoapps
npx create-react-app frontend
yarn run build
```

#### ReactJS Integration to Django

The following three files are the key to tightly integrating the ReactJS app to the Django templating system.

- [django_with_react/djangoapps/frontend/views.py](https://github.com/lpm0073/django_with_react/blob/main/django_with_react/djangoapps/frontend/views.py)
- [django_with_react/djangoapps/frontend/templates/index.html](https://github.com/lpm0073/django_with_react/blob/main/django_with_react/djangoapps/frontend/templates/index.html)
- [config/settings/base.py](https://github.com/lpm0073/django_with_react/blob/main/config/settings/base.py#L338)
#### Additional Django Settings
The following is added to `settings/base.py` in order to integrate static asset collection into Django templating:

```Python
FRONTEND_DIR = APPS_DIR / "djangoapps/frontend"
STATICFILES_DIRS += [
    str(FRONTEND_DIR / "build/static"),
    str(FRONTEND_DIR / "public/assets"),
]
WHITENOISE_ROOT = FRONTEND_DIR / "build"
```
#### Running

The React app runs inside of Django and therefore **does not** require a node dev server running on port 3000.
**However, you do need to run Django's manage.py collectstatic in order to copy the ReactJS asset-manifest.json file into a location where the Django templating system can open and read it at run-time.**

```bash
docker-compose -f local.yml up --build
docker-compose -f local.yml run --rm django python manage.py collectstatic
```
navigate to http://localhost:8000/app/



## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands


For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy django_with_react

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd django_with_react
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Docker Deployment

The following details how to deploy this application. See detailed [cookiecutter-django Docker Development documentation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html).


## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy django_with_react

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd django_with_react
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss), or get explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).
