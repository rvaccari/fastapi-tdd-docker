help:
	@echo -e "lint             Lint the project for coding standards. Recommended to run before pushing to remote (adding a git pre-commit hook must be nice ;)"
	@echo -e "format           Format the project for coding standards black"
	@echo -e "docker-build     Start build docker-compose"
	@echo -e "docker-up        Start all the environment on docker-compose"
	@echo -e "docker-down      Stop docker-compose environment"
	@echo -e "docker-test      Run the full teste suite in Docker. IMPORTANT: You must have a database named "web_test" created to successfully run them"

docker-build:
	docker-compose up -d --build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down -v

docker-test:
	docker-compose exec web python -m pytest

docker-test-parallel:
	docker-compose exec web pytest -k "unit" -n auto

test:
	pytest -ra --disable-warnings --color=yes $(ARGS)

test-parallel:
	$(eval ARGS ?= -k "unit" -n auto $(EXTRA_ARGS))
	make test ARGS="$(ARGS)"

lint:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -f .coverage
	#make test ARGS="--cov=project --cov-fail-under=70 $(ARGS)"
	make test ARGS="--cov=. --cov-fail-under=70 --pydocstyle --mypy --black $(ARGS)"

format:
	black app tests