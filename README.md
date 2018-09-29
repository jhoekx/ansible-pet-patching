# Ansible Pet Patching

This repository contains a web application that shows the patching status of RPM based systems that are managed by Ansible.

## Development

```bash
$ python -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ FLASK_ENV=development FLASK_APP=app.py flask run
```

Ansible inventory data will be searched for in the `inventory` directory.

The application listens on port `5000` by default.

## Docker

A docker build file is provided that creates a basic container.

```
$ docker build -t ansible-pet-patching .
```

Mount the inventory directory at `/srv/http/app/inventory`.
The application exposes port 8000.

It is expected that the real production container extends this container to provide secrets to Ansible.
