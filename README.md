# Workout Tracker Website API - work in progress

Workout planning and tracking website's API.

Application Exercises data was acquired from [Open Public Domain Exercise Dataset in JSON format](https://github.com/wrkout/exercises.json)

## Usage

1. Clone repository: `git clone git@github.com:tvrbosic/workout-tracker-api.git`
2. Install project requirements: `cd workout-tracker-website-api && pip install -r requirements.txt`
3. Apply database migrations: `python3 manage.py migrate`
4. Create database superuser: `python3 manage.py createsuperuser`
5. Run app: `python3 manage.py runserver`
6. Visit to check if app is running: `http://localhost:8000/`

## API features

- Implemented using [Django REST Framework](https://www.django-rest-framework.org)
- JWT authentication and authorization
- Custom user model
- Endpoints for executing CRUD operations: Muscles, Categories, Exercises, Workouts, Programs, Planner
- Prepared basic data fixtures for testing
- User can create own workouts and programs
- Workouts and programs can be added to planer (data suitable to be added and displayed in calendars)

## Superuser credentials

- Email: `admin@email.com`
- Password: `Superuserpassword0!`
