# API Testing Portfolio Project

This is a standalone API testing example project. It contains a small FastAPI service used as a stable system under test, plus a pytest-based API test framework around it.

## What This Demonstrates

- Python application code with FastAPI and Pydantic models
- API CRUD testing with pytest
- Positive, negative, and boundary tests
- Fixtures in `conftest.py`
- Reusable API client wrapper
- Test data loaded from JSON
- Response schema validation
- Authentication and authorization checks
- GitHub Actions workflow for CI

## Project Structure

```text
01-api-tests/
|-- src/
|   `-- qa_store_api/
|-- tests/
|   |-- data/
|   |-- schemas/
|   |-- conftest.py
|   |-- test_auth_api.py
|   |-- test_orders_api.py
|   `-- test_products_api.py
|-- requirements.txt
|-- pytest.ini
`-- README.md
```

## Run Locally

```powershell
cd python\01-api-tests
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

Run the demo API:

```powershell
uvicorn qa_store_api.main:app --app-dir src --reload
```

Open API docs:

- http://127.0.0.1:8000/docs

## Test Coverage

| Test file | Focus |
| --- | --- |
| `test_auth_api.py` | Login, token validation, unauthorized access |
| `test_products_api.py` | Product listing, filtering, and not-found behavior |
| `test_orders_api.py` | Order CRUD flow, validation, status changes, schema checks |
