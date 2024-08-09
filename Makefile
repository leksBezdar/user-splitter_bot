D = docker
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
STORAGES_FILE = docker_compose/storages.yaml
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = aiohttp_app
DB_CONTAINER = postgres_splitter


.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} down

.PHONY: postgres
postgres:
	${EXEC} ${DB_CONTAINER} psql -U ${DB_USER} -d ${DB_NAME} -p ${DB_PORT}

.PHONY: revision
revision:
	@if [ -z "${name}" ]; then echo "Description is required. Usage: make revision name=\"description\""; exit 1; fi
	${EXEC} ${APP_CONTAINER} alembic revision --autogenerate -m "${name}"

.PHONY: upgrade
upgrade:
	${EXEC} ${APP_CONTAINER} alembic upgrade head

.PHONY: downgrade
downgrade:
	${EXEC} ${APP_CONTAINER} alembic downgrade -1

.PHONY: all
all:
	${DC} -f ${STORAGES_FILE} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} -f ${APP_CONTAINER}

.PHONY: shell
shell:
	${D} exec -it ${APP_CONTAINER} bash
