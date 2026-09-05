import sqlite3

import pytest


@pytest.fixture
def database_connection():
    # EN: The fixture creates an isolated database for every test.
    # RU: Фикстура создает изолированную базу данных для каждого теста.
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        create table orders (
            id integer primary key,
            customer text not null,
            status text not null,
            total real not null check(total > 0)
        )
        """
    )
    yield connection
    connection.close()
