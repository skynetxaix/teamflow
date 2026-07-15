# TeamFlow

A team task management system built with Django, designed around a modular multi-app architecture.

## Project Status
This project is under active development. Core models and app structure are in place; 
UI, authentication flow, and task-assignment features are being completed over the coming days.

## Overview
TeamFlow helps teams organize projects and track tasks through a clean, modular backend.
The project is split into separate Django apps to keep responsibilities isolated and the
codebase easy to extend.

## Architecture
- **projects/** — project creation and management
- **tasks/** — task creation, assignment, and status tracking
- **users/** — user accounts and roles
- **core/** — shared utilities and base configuration

## Tech Stack
- Python / Django
- Multi-app architecture (separation of concerns)

## What's working
- [x] Project structure and app separation
- [x] Core data models

## What's coming
- [ ] Task assignment and status workflow
- [ ] User roles and permissions
- [ ] Templates / frontend
- [ ] Deployment

## Setup
```bash
git clone https://github.com/skynetxaix/teamflow.git
cd teamflow
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---
coming soon...
