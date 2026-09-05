# JMeter Load Testing Examples

This folder is for JMeter test plans that demonstrate load testing beyond ordinary web UI checks.

Included examples:

- `jdbc-load-test-plan.jmx` - template for database load testing through JDBC.
- `tcp-load-test-plan.jmx` - template for TCP protocol load testing.

These plans are intentionally small and readable. In a real project, the same structure can be extended with environment-specific variables, CSV data sets, backend listeners, and HTML report publishing.

Useful JMeter concepts shown here:

- Thread groups
- Ramp-up configuration
- Non-HTTP samplers
- Assertions
- Result collection
- Parameterized environment variables

Run a plan from the command line:

```powershell
jmeter -n -t python/04-load-tests/jmeter/jdbc-load-test-plan.jmx -l output/jmeter/results.jtl -e -o output/jmeter/html
```
