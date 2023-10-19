# Architect_Task_Project

# Task Manager Application

This is a simple Django application that allows users to manage a list of tasks using a RESTful API.

## Setup Instructions

1. Install Python and Django (if not already installed):
pip install django djangorestframework


2. Run the migrations:
python manage.py makemigrations
python manage.py migrate


3. Create a superuser to access the Django admin:
python manage.py createsuperuser


4. Run the server:
python manage.py runserver

5. Access the application at http://127.0.0.1:8000/

## API Endpoints

- **List Tasks**: GET /tasks/
- **Create Task**: POST /tasks/
- **Retrieve Task**: GET /tasks/{id}/
- **Update Task**: PUT /tasks/{id}/
- **Delete Task**: DELETE /tasks/{id}/
