# Flask Web Application

## Overview
A simple Flask web application with user authentication and profile management. The project uses Flask-WTF for forms, SQLAlchemy for database management, and Bootstrap for a clean UI.

## Features
- User Registration
- User Login and Logout
- Profile Update (Username, Email, Password)
- Authentication and Authorization

## Project Structure
```
project/
├── app/
│   ├── __init__.py          # Initialize app and configure extensions
│   ├── models.py            # Database models
│   ├── routes.py            # Application routes
│   ├── forms.py             # Forms for user interaction
│   ├── templates/           # HTML templates
│       ├── base.html        # Base template
│       ├── home.html        # Profile page
│       ├── login.html       # Login page
│       ├── register.html    # Registration page
├── instance/
│   ├── site.db              # SQLite database
├── create_user_table.py     # Script to manually create tables
├── run.py                   # Application entry point
├── requirements.txt         # Dependencies
```

## Requirements
- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-Bcrypt
- Flask-Login
- Flask-WTF
- email-validator

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python create_user_table.py
   ```

5. Run the application:
   ```bash
   python run.py
   ```

6. Open the application in your browser:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
- Register a new user.
- Login with your credentials.
- Update your profile on the home page.

## License
This project is licensed under the MIT License.

