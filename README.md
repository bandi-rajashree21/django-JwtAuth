### This project demonstrates how to implement JWT (JSON Web Token) Authentication using Django REST Framework and SimpleJWT.

# Install Dependencies
- `pip install django`
- `pip install djangorestframework`
- `pip install djangorestframework_simplejwt`

# Project Setup

## 1. Apply Migrations
```bash
python manage.py migrate
```

## 2. Create Superuser
```bash
python manage.py createsuperuser
```
> **Note:** You will be prompted to enter a username, email, and password.

## 3. Run Server
```bash
python manage.py runserver
```
The server will be running at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

# JWT Endpoints

## Obtain Access & Refresh Token
**Endpoint:** `POST /api/token/`
### Request Body:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
### Response:
```json
{
  "refresh": "refresh_token_here",
  "access": "access_token_here"
}
```

## Refresh Access Token
**Endpoint:** `POST /api/token/refresh/`
### Request Body:
```json
{
  "refresh": "your_refresh_token"
}
```
### Response:
```json
{
  "access": "new_access_token"
}
```

## Protected Endpoint
**Endpoint:** `GET /hello/`
### Header:
authorization: Bearer `<access_token>`
### Response:
```json
{
  "message": "Hello, Rajashree"
}
