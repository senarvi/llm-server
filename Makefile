.PHONY: test clean

clean:
	rm -rf .pytest_cache

test: clean
	pytest tests -v

format:
	pyupgrade --py36-plus *.py */*.py */*/*.py || true
	isort .
	black . --exclude .vscode
