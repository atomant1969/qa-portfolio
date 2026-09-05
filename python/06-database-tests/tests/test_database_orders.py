import pytest


pytestmark = pytest.mark.database


def test_order_table_schema_contains_expected_columns(database_connection):
    columns = {row[1]: row[2] for row in database_connection.execute("pragma table_info(orders)")}

    assert columns == {"id": "INTEGER", "customer": "TEXT", "status": "TEXT", "total": "REAL"}


def test_order_aggregate_matches_expected_business_metric(database_connection):
    database_connection.executemany(
        "insert into orders(customer, status, total) values (?, ?, ?)",
        [
            ("Robert Joyce", "paid", 100.0),
            ("Second Customer", "paid", 150.0),
            ("Third Customer", "cancelled", 40.0),
        ],
    )

    paid_total = database_connection.execute("select sum(total) from orders where status = 'paid'").fetchone()[0]

    assert paid_total == 250.0
