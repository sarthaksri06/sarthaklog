# Authentication System

A secure authentication system with login, signup, and dashboard functionality built with Flask.

## Quick Start

```bash
# Install dependencies
pip install flask flask-cors pyjwt werkzeug

# Run the application
python app.py

# Open browser
http://127.0.0.1:5000
Features
User registration and login

Password hashing for security

JWT token authentication

Protected dashboard routes

Password reset functionality

Session management

Project Structure
SRTKLOGINDASH/
├── app.py              # Main application
├── database.py         # Database operations
├── requirements.txt    # Python dependencies
├── templates/          
│   ├── login.html      # Login and signup page
│   └── dashboard.html  # User dashboard
└── static/
    └── style.css       # Stylesheet
API Endpoints
Endpoint	Method	Description
/signup	POST	Create new account
/login	POST	Authenticate user
/logout	POST	End session
/forgot-password	POST	Request password reset
/api/dashboard	GET	Get user data

Database
The application uses SQLite. The database file users.db is created automatically on first run.
Database schema:
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Technology Stack
Backend: Flask (Python)

Database: SQLite

Authentication: JWT

Security: Werkzeug

Frontend: HTML5, CSS3, JavaScript

License
MIT





