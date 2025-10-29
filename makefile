dev:
	ENV=dev uv run --active uvicorn src.main:app --reload

uat:
	ENV=uat uv run --active uvicorn src.main:app --reload

prod:
	ENV=prod uv run --active uvicorn src.main:app --reload