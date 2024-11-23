# Spoty

This repository contains the backend implementation for Spoty app. 

## 🚀 Technologies Used

- Backend Framework: Django
- Database: sqlite

## Installation

Install db-assignment with git

```bash
    git clone https://github.com/matonyn/nfactorial-task.git
    cd nfactorial-task
```
    



## Run Locally

Clone the project

```bash
    git clone https://github.com/matonyn/nfactorial-task.git
```

Go to the project directory

```bash
    cd nfactorial-task
```

Create virtual environment

```bash
    python -m venv venv
    source venv/bin/activate
```

Install dependencies:

```bash
    pip install -r requirements.txt
```
Set up the database: ```Use .env for environment variables.```

Apply migrations:

```bash
    python manage.py migrate
```

Run the development server:
```bash
    python manage.py runserver
```

Access the application at ``` http://127.0.0.1:8000/.```
