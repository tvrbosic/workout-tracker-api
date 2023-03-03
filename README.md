# Workout Tracker Website API

Workout planning and tracking website's API.

## Usage

1. Clone repository: `git clone git@github.com:tvrbosic/workout-tracker-api.git`
2. Install project requirements: `cd workout-tracker-website-api && pip install -r requirements.txt`
3. Apply database migrations: `python3 manage.py migrate`
4. Create database superuser: `python3 manage.py createsuperuser --email admin@email.com --username admin`
5. Run app: `python3 manage.py runserver`
6. Visit to check if app is running: `http://localhost:8000/`

## Superuser credentials

- Username: `admin`
- Password: `admin`
