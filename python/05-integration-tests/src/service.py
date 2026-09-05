from uuid import uuid4

from src.repository import OrderRepository


class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self.repository = repository

    def create_order(self, customer: str, product: str) -> dict[str, object]:
        order = {
            "id": str(uuid4()),
            "customer": customer,
            "product": product,
            "status": "created",
        }
        self.repository.save(order["id"], order)
        return order
