up:
	docker-compose up

build:
	docker-compose build

psql:
	docker-compose exec web-db psql -U postgres

test:
	docker-compose exec web python -m pytest

initdb:
	docker-compose exec web python app/db.py
