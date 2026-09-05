# Python QA Portfolio

This directory mirrors the full QA portfolio map. Each numbered folder is treated as its own standalone Python mini-project with its own tests and setup files.

## Structure

```text
python/
|-- 01-api-tests/
|-- 02-ui-tests/
|-- 03-e2e-tests/
|-- 04-load-tests/
|-- 05-integration-tests/
|-- 06-database-tests/
|-- 07-security-tests/
|-- 08-mobile-tests/
|-- 09-performance-tests/
|-- 10-test-utilities/
|-- 11-ci-cd/
|-- 12-ai-assisted-testing/
`-- 13-documentation/
```

## Recruiter Feedback Coverage

| Requirement | Evidence |
| --- | --- |
| Python application development | `01-api-tests/src/qa_store_api/` contains a small FastAPI service with typed models and business rules. |
| Load testing of non-web systems | `04-load-tests/jmeter/` contains JDBC and TCP JMeter plan examples. |
| Statistical data analysis | `09-performance-tests/` and `10-test-utilities/analyze_test_results.py` calculate pass rate, failure rate, mean, median, and p95 duration. |
| Workflow automation with AI | `12-ai-assisted-testing/` contains repeatable AI-assisted QA workflows for logs, test ideas, bug reports, and regression impact analysis. |

## Current Contents

| Directory | Current status |
| --- | --- |
| `01-api-tests/` | Working pytest API tests for the demo FastAPI app. |
| `02-ui-tests/` | Scaffold for future Playwright or Selenium Python UI tests. |
| `03-e2e-tests/` | Placeholder for API + UI scenarios. |
| `04-load-tests/` | JMeter examples for JDBC and TCP load testing. |
| `05-integration-tests/` | Working cross-layer order lifecycle test. |
| `06-database-tests/` | Placeholder for SQL validation and migration checks. |
| `07-security-tests/` | Placeholder for OWASP-style security checks. |
| `08-mobile-tests/` | Placeholder for mobile automation examples. |
| `09-performance-tests/` | Working statistical quality metric test. |
| `10-test-utilities/` | Python CLI utilities for data generation and test result analysis. |
| `11-ci-cd/` | GitHub Actions workflow example. |
| `12-ai-assisted-testing/` | Documented AI-assisted QA workflows. |
| `13-documentation/` | QA documentation examples with tests that validate document quality. |

## How To Run

```powershell
cd python\01-api-tests
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

For another project, enter that numbered directory and use its local `requirements.txt` and `pytest.ini`.

Example API app run command:

```powershell
cd python\01-api-tests
uvicorn qa_store_api.main:app --app-dir src --reload
```

Then open:

- API docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## Portfolio Roadmap

- Expand Playwright Python UI tests under `02-ui-tests/`.
- Expand API + UI end-to-end scenarios under `03-e2e-tests/`.
- Add PostgreSQL examples under `06-database-tests/`.
- Add Allure or pytest-html reports under `13-documentation/`.
- Add Docker Compose for PostgreSQL and a runnable JDBC load-test target.
