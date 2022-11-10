# run homework
.PHONY: homework-i-run
homework-i-run:
	@python manage.py runserver

# install requirements
.PHONY: init-dev
init-dev:
	@python -m pip install --upgrade pip
	pip -requirement requirements.txt

# Run tools for files from commit.
.PHONY: pre-commit-run
pre-commit-run:
	@pre-commit run

# Run tools for all files.
.PHONY: pre-commit-run-all
pre-commit-run-all:
	@pre-commit run --all-files

# Init superuser (admin)
.PHONY: init-dev-i-create-superuser
init-dev-i-create-superuser:
	@DJANGO_SUPERUSER_PASSWORD=admin1234 python manage.py createsuperuser --user admin1 --email admin@gmail.com --no-input

# Kill all process on port 8000
.PHONY: util-i-kill-by-port
util-i-kill-by-port:
	@sudo lsof -i:8000 -Fp | head -n 1 | sed 's/^p//' | xargs sudo kill

.PHONY: init-config
# Init config files
init-config:
	@cp docker-compose.override.homework.yml docker-compose.override.yml

.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	@make init-config && \
		make d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge


.PHONY: d-run
# Just run with docker
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose \
			up --build


.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose \
			down --volumes --remove-orphans --rmi local --timeout 0

.PHONY: migrations
# Make migrations
migrations:
	@python manage.py makemigrations

.PHONY: migrate
# Migrate
migrate:
	@python manage.py migrate