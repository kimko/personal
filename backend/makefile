k?=test

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
ifeq ($(k),cov)
	@echo "ALL TESTS WITH COVERAGE"
	docker-compose exec web python -m pytest --cov="." --cov-report html
else
	@echo "VERBOSE WITH PATTERN $(k)"
	docker-compose exec web python -m pytest -vvl -k $(k)
endif

initdb:
	docker-compose exec web python app/db.py

initdb-prod:
	heroku run python app/db.py --app $(HEROKU_APP)
