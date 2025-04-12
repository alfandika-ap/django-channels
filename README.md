# Django Channels Project

This is a Django application using Django Channels for real-time functionality.

## Features

- Real-time notifications using WebSockets
- Django 5.2
- Channels 4.2.2 with Redis backend
- Background task processing with Huey

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Make sure Redis is running (required for Channels)
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

## Project Structure

- `core/`: Core application
- `notifications/`: Notification handling app with Channels consumers
- `manage.py`: Django management script

## WebSocket Connections

WebSocket connections are handled through Django Channels and can be accessed at:
```
ws://localhost:8000/ws/notifications/
```

## Background Tasks

This project uses Huey for background task processing. Start the Huey consumer with:
```
python manage.py run_huey
``` 