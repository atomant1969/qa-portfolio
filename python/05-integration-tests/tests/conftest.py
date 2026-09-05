import pytest

from src.repository import OrderRepository
from src.service import OrderService


@pytest.fixture
def repository() -> OrderRepository:
    return OrderRepository()


@pytest.fixture
def order_service(repository: OrderRepository) -> OrderService:
    return OrderService(repository)
