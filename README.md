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
text
├── app.py              # Backend server
├── templates/          
│   ├── login.html      # Authentication pages
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
Technology Stack
Backend: Flask (Python)

Authentication: JWT

Security: Werkzeug
Technology Stack
Backend: Flask (Python)

Database: SQLite

Authentication: JWT

Security: Werkzeug

Frontend: HTML5, CSS3, JavaScript

License
MIT



