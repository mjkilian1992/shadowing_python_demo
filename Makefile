start:
	docker compose up

stop:
	docker compose down

test:
	docker compose run --rm app pytest

makemigrations:
	docker compose run --rm app python manage.py makemigrations

migrate:
	docker compose run --rm app python manage.py migrate

shell:
	docker compose run --rm app python manage.py shell -i ipython

createsuperuser:
	docker compose run --rm app python manage.py createsuperuser

frontend-install:
	cd frontend && npm install

css-watch:
	cd frontend && npm run css-watch