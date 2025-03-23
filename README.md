# FC-Clubs Application
FC-Clubs is application from create catalog football clubs, players and manager

# Used
Python, Django, Mysql and Docker 

## Installation
Use the Docker for installation application

## Usage
Starting
```bash
docker compose up -d
```
First use you need make migrations
```bash
# Go to web container
docker compose exec web bash
# Create migrations
python manage.py makemigrations
# Running migrations
python manage.py migrate
```