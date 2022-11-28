mode=?

build:
	docker-compose build

start:
	docker-compose -f docker-compose.yml -f docker-compose.${mode}.yml up -d

attach:
	docker exec -it deepstream-rtsp bash

clean:
	docker-compose down --remove-orphans