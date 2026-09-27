# Gym Management System

A simple Django and SQLite college project for managing gym members, membership plans, and daily check-ins.

## Run the project

```bash
source .venv/bin/activate
python manage.py migrate
python manage.py seed_gym_data
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.

## Useful commands

- `python manage.py seed_gym_data` — creates Basic, Standard, and Premium plans, four members, and sample attendance. It is safe to rerun.
- `python manage.py createsuperuser` — creates an administrator account for `/admin/`.

## Features

- Dashboard statistics calculated from the SQLite database
- Member, plan, and attendance CRUD operations
- Member name/phone search
- Duplicate same-day check-in prevention
- Membership date and attendance-time validation
- Responsive fitness-themed interface and Django admin configuration
