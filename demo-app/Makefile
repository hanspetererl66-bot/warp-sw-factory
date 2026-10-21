.PHONY: test lint smoke run

test:
	python3 -m unittest discover -s tests -t .

lint:
	python3 -m compileall -q quote_service tests

run:
	python3 -m quote_service.server

# make smoke URL=https://staging.example.com
smoke:
	@test -n "$(URL)" || (echo "URL is required"; exit 2)
	curl -fsS "$(URL)/health"
