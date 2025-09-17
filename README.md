# chatMCA

A Django-based AI chat application project.

## Features
- Real-time chat interface (see `templates/chat.html`)
- Django backend (see `core/`)
- SQLite database (`db.sqlite3`)

## Project Structure
```
chatMCA/
├── Files/         # Django project settings
├── core/            # Main app (models, views, admin)
├── templates/       # HTML templates
├── db.sqlite3       # SQLite database
├── manage.py        # Django management script
```

## Getting Started
1. Install dependencies:
   ```bash
   pip install django
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the development server:
   ```bash
   python manage.py runserver
   ```
4. Open `http://127.0.0.1:8000/` in your browser.

## Usage
- Access the chat interface at `/chat/` (see `chat.html` template).

## License
This project is for educational purposes.
