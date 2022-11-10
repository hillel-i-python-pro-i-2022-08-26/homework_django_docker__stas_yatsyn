# Homework contacts and commands Stas Yatsyn

***

[![Main workflow](https://github.com/hillel-i-python-pro-i-2022-08-26/homework_django_contacts_and_commands__stas_yatsyn/actions/workflows/main-workflow.yml/badge.svg)](https://github.com/hillel-i-python-pro-i-2022-08-26/homework_django_contacts_and_commands__stas_yatsyn/actions/workflows/main-workflow.yml)

### Main commands:

* `make homework-i-run` - *start project*
* `make init-dev` - *install requirements*
* `make pre-commit-run-all` - *run pre-commit tool for all files*
* `python manage.py generate_info NUMBER` - *generate required amount of users (by default 10)*
* `python manage.py generate_info -i or --ignore NUMBER` - *generate required amount of users (by default 10) and set
  is_auto_generated field in model to False*
* `python manage.py delete_info` - *delete auto generate users info*
* `python manage.py delete_info --all` - *delete ALL users info*
* `make init-dev-i-create-superuser` - *create superuser for admin access*
* `make d-homework-i-run` - *start project in docker*
* `d-homework-i-purge` - *make all actions needed for purge homework related data.*
* `/session/` - *view user session info*
1) View session key
2) View number of visits
3) View last time of user visit