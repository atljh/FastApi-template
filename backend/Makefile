CONTAINER_NAME = fastapi

run:
	docker-compose up -d $(CONTAINER_NAME)

stop:
	docker-compose stop $(CONTAINER_NAME)

remove:
	docker-compose rm -f $(CONTAINER_NAME)

logs:
	docker-compose logs -f $(CONTAINER_NAME)

restart: stop remove run

build:
	docker-compose build $(CONTAINER_NAME)

rebuild: stop remove build run


.PHONY: run stop remove logs restart build rebuild