K?=test

up:
	docker-compose up

build:
	docker-compose build

build-prod:
	docker build -f project/Dockerfile.prod -t registry.heroku.com/$(HEROKU_APP)/web ./project

deploy-prod:
	heroku container:login
	docker push registry.heroku.com/$(HEROKU_APP)/web:latest
	heroku container:release web --app $(HEROKU_APP)
	heroku logs --tail

psql:
	docker-compose exec web-db psql -U postgres

test:
	docker-compose exec web python -m pytest -vvl -k $(K)

initdb:
	docker-compose exec web python app/db.py
