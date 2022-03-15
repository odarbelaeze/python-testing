import pytest
from sqlalchemy.future.engine import Connection, Engine, create_engine
from sqlalchemy.sql.expression import text


@pytest.fixture()
def engine() -> Engine:
    return create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


def test_basic_text_execution(engine: Engine):
    connection: Connection
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 'hello world'"))
        assert result.all() == [("hello world",)]


@pytest.fixture()
def connection(engine: Engine):
    with engine.connect() as connection:
        yield connection


def test_connection_text_execution(connection: Connection):
    result = connection.execute(text("SELECT 'hello world'"))
    assert result.all() == [("hello world",)]


def test_fixtures_are_created_once(connection: Connection, engine: Engine):
    assert connection.engine is engine
