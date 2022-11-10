FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

# Copy_project_files__start
COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt



COPY --chown=${USER} --chmod=755 ./docker/app/start.sh /start.sh
COPY --chown=${USER} --chmod=755 ./docker/app/entrypoint.sh /entrypoint.sh

COPY --chown=${USER} ./manage.py manage.py
COPY --chown=${USER} ./Makefile Makefile

# Copy_project_files__stop

# Copy_apps__start
COPY --chown=${USER} ./core core
COPY --chown=${USER} ./admin_users admin_users
COPY --chown=${USER} ./base base
COPY --chown=${USER} ./greetings greetings
COPY --chown=${USER} ./phone_book phone_book
COPY --chown=${USER} ./users_generator users_generator
COPY --chown=${USER} ./session_app session_app
# Copy_apps__stop

# Copy_visual__start
COPY --chown=${USER} ./templates templates
# Copy_visual__stop

USER ${USER}

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]