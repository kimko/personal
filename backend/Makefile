k?=test

up:
	docker-compose up

upnew:
	docker-compose up  --force-recreate

build:
	docker-compose build

build-prod:
	docker build -f project/Dockerfile.prod -t registry.heroku.com/$(HEROKU_APP)/web ./project

build-gha:
	docker build -f project/Dockerfile -t docker.pkg.github.com/kimko/personal/backend:latest ./project
	docker login docker.pkg.github.com -u kimko -p $(GHA_TOKEN)
	docker push docker.pkg.github.com/kimko/personal/backend:latest

psql-dev:
	docker-compose exec web-db psql -U postgres

psql-prod:
	 heroku pg:psql

test:
ifeq ($(k),cov)
	@echo "ALL TESTS WITH COVERAGE"
	docker-compose exec web black .
	docker-compose exec web isort . --profile black
	docker-compose exec web python -m pytest --cov="." --cov-report html
else
	@echo "VERBOSE WITH PATTERN $(k)"
	docker-compose exec web python -m pytest -vvl -k $(k)
endif

migrate:
	docker-compose exec web aerich migrate

init-dev:
	docker-compose exec web aerich init -t db.TORTOISE_ORM
	docker-compose exec web aerich upgrade
	docker-compose exec web aerich -c aerich_test.ini upgrade

upgrade-dev:
	docker-compose exec web aerich upgrade
	docker-compose exec web aerich -c aerich_test.ini upgrade


upgrade-prod:
	heroku run python app/models/db.py migrate

lint:
	docker-compose exec web flake8 .
	docker-compose exec web black . --check
	docker-compose exec web isort . --check-only --profile black
