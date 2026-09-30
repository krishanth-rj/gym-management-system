# Gym Management System

A Django-based gym management application for tracking members, plans, attendance, and dashboard insights in a simple, user-friendly interface.

## Live Demo

The project is deployed and running here:

https://gym-management-system-63h0.onrender.com/

## Overview

This application helps manage a fitness center by allowing staff to:

- track member records
- manage membership plans
- record daily attendance
- view dashboard statistics
- prevent duplicate check-ins for the same day
- maintain a clean admin workflow for operations

## Tech Stack

- Python
- Django
- SQLite for local development
- HTML/CSS templates
- Django admin

## Features

- Dashboard statistics calculated from application data
- Add, edit, and delete members
- Manage gym plans and pricing tiers
- Track attendance logs and daily check-ins
- Search members by name or phone number
- Prevent duplicate same-day attendance entries
- Validate member dates and attendance times
- Responsive, fitness-themed UI

## Local Setup

```bash
git clone <repository-url>
cd djangoprojects
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_gym_data
python manage.py runserver
```

Then open:

http://127.0.0.1:8000/

## Useful Commands

- `python manage.py seed_gym_data` — creates sample plans, members, and attendance data. Safe to run multiple times.
- `python manage.py createsuperuser` — creates an administrator account for the Django admin panel at `/admin/`.
- `python manage.py migrate` — applies database migrations.
- `python manage.py runserver` — starts the development server.

## Admin Panel

After creating a superuser, you can log in at:

http://127.0.0.1:8000/admin/

This is useful for managing records directly through Django's built-in administrative interface.

## Notes

- The project is designed for a college/portfolio-style gym management workflow.
- The sample data command loads example plans and records to make the dashboard and screens easier to test.
- The live deployment is hosted on Render, while the local development version uses the default SQLite setup.
