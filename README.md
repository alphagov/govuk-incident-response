# GOV.UK Incident Response

Experiment trying out Monzo's Response tool.

## Installing

```sh
$ pipenv install
```

## Running

```sh
$ pipenv run python manage.py migrate
$ pipenv run python manage.py runserver
```

## Deploying

```sh
$ pipenv lock -r > requirements.txt
$ cf push govuk-incident-response
```
