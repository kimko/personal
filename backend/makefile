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
	docker-compose exec web black .
	docker-compose exec web isort . --profile black
	docker-compose exec web python -m pytest --cov="." --cov-report html
else
	@echo "VERBOSE WITH PATTERN $(k)"
	docker-compose exec web python -m pytest -vvl -k $(k)
endif

initdb:
	docker-compose exec web python app/db.py

initdb-prod:
	heroku run python app/db.py --app $(HEROKU_APP)

lint:
	docker-compose exec web flake8 .
	docker-compose exec web black . --check
	docker-compose exec web isort . --check-only --profile black
