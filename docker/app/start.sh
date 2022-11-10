#!/usr/bin/env bash

# Bash_init__start
# Exit whenever it encounters an error, also known as a non–zero exit code.
set -o errexit
# Return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status,
#   or zero if all commands in the pipeline exit successfully.
set -o pipefail
# Treat unset variables and parameters other than the special parameters ‘@’ or ‘*’ as an error when performing parameter expansion.
set -o nounset
# Print a trace of commands.
set -o xtrace
# Bash_init__stop

# Apply database migrations.
make migrate

# Run application.
python manage.py runserver 0.0.0.0:8000