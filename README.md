# flask-project-template
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

This repository contains the basic structure of a Flask project.

## Python Version

It is recommended to use the latest version of Python. Flask is compatible with Python 3.7 and later.

## Getting Started

Clone the project.

```bash
  git clone
```
Go to the project directory.

```bash
  cd flask-project-template
```

## Virtual environment

In the project folder run the following command to create a virtual environment:

```bash
  python3 -m venv venv
```

## Activate the environment

Before you work on your project, activate the corresponding environment:

```bash
  source venv/bin/activate
```

## Install requirements.txt

You can install `requirements.txt` or flask directly with the following commands:

```bash
  pip install -r requirements.txt
```

```bash
  pip install flask
```

## Debugging and development in Flask

To set up the project environment for development and debugging, run the following commands in your bash shell:

```bash
  export FLASK_DEBUG=1
```

```bash
  export FLASK_ENV=development
```

## Start the server

```bash
  flask run
```

## Documentation

[Flask documentation](https://flask.palletsprojects.com/en/2.1.x/)

## Author

- [@jorfanpabon](https://www.github.com/jorfanpabon)
