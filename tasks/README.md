# Task Manager API

A production-ready REST API built with Django REST Framework for managing personal tasks.

## Features
- User registration and JWT authentication
- Full CRUD operations for tasks
- Filter tasks by status
- Search tasks by title or description
- Order tasks by date or status
- Pagination (3 tasks per page)
- Custom validation on all inputs
- Consistent error response format

## Tech Stack
- Django + Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- django-filter

## Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /api/auth/register/ | Register a new user | No |
| POST | /api/auth/login/ | Login, get JWT tokens | No |
| POST | /api/auth/refresh/ | Refresh access token | No |
| GET | /api/tasks/ | List your tasks | Yes |
| POST | /api/tasks/ | Create a task | Yes |
| GET | /api/tasks/{id}/ | Get a single task | Yes |
| PATCH | /api/tasks/{id}/ | Update a task | Yes |
| DELETE | /api/tasks/{id}/ | Delete a task | Yes |

## Query Parameters

| Parameter | Example | Description |
|-----------|---------|-------------|
| status | ?status=pending | Filter by status |
| search | ?search=django | Search title/description |
| ordering | ?ordering=-created_at | Order results |
| page | ?page=2 | Paginate results |

## Setup
1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install packages: `pip install -r requirements.txt`
5. Create `.env` file with your own values
6. Run migrations: `python manage.py migrate`
7. Start server: `python manage.py runserver`

## Environment Variables
```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=taskapi_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```