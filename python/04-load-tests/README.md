# Load Testing Portfolio Project

Standalone load testing project for non-web targets.

Contents:

- `jmeter/jdbc-load-test-plan.jmx` - JDBC/database load testing plan
- `jmeter/tcp-load-test-plan.jmx` - TCP protocol load testing plan
- `tests/` - pytest checks that validate the JMeter plans as portfolio artifacts

```powershell
cd python\04-load-tests
pip install -r requirements.txt
pytest
```
