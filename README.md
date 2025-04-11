# ToDoList

## Overview
ToDoList is simple website, made for practice, created for managing tasks and tags.

## Features
- Django 5.1.5

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- PostgreSQL (or SQLite for development)
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Setup

#### Clone the repository
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

#### Configure project
```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```


## Pages
Below are some key pages:

| Method | Endpoint            | Description            |
|--------|---------------------|------------------------|
| GET   | `/`  | Home page            |
| GET   | `/tags/` | Tag Page |


## Running Tests
```bash
# Run all tests
python manage.py test tests
```

