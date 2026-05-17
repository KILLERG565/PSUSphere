# PSUSphere

A student organization management system for Pangasinan State University.

## Features

- Manage Colleges, Programs, Organizations, Students, and Memberships
- Bootstrap 5 dashboard with sidebar navigation
- Django Admin with search, filters, and list views
- Fake data seeder using Faker

## Tech Stack

- Python 3.10+
- Django 4.2
- Bootstrap 5.3
- SQLite (development)

## Setup

```bash
# 1. Clone and enter the repo
git clone <your-repo-url> PSUSphere
cd PSUSphere

# 2. Create and activate virtual environment
python -m venv psusenv
source psusenv/bin/activate        # Linux/macOS
psusenv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
cd projectsite
python manage.py makemigrations
python manage.py migrate

# 5. Seed the database
python manage.py create_initial_data

# 6. Create superuser
python manage.py createsuperuser

# 7. Run the server
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Authors

- Gabriel Avanceña
