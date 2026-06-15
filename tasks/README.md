# Task Manager API

A REST API built with Django REST Framework for managing personal tasks.

## Features
- User registration and JWT authentication
- CRUD operations for tasks
- Each user can only access their own tasks

## Tech Stack
- Django + Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)

## Endpoints
| Method | Endpoint | Description |
|--------|----------|--------------|
| POST | /api/auth/register/ | Register a new user |
| POST | /api/auth/login/ | Login, get JWT tokens |
| GET | /api/tasks/ | List your tasks |
| POST | /api/tasks/ | Create a task |
| GET | /api/tasks/{id}/ | Get a single task |
| PATCH | /api/tasks/{id}/ | Update a task |
| DELETE | /api/tasks/{id}/ | Delete a task |

## Setup
1. Clone the repo
2. Create virtual environment and activate it
3. `pip install -r requirements.txt`
4. Create `.env` file with your own values
5. Run migrations: `python manage.py migrate`
6. Run server: `python manage.py runserver`