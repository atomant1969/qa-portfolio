from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Order:
    id: str
    customer: str
    total: float
    status: str


class OrderService:
    def __init__(self) -> None:
        self.orders: dict[str, Order] = {}

    def create_order(self, customer: str, total: float) -> Order:
        order = Order(id=str(uuid4()), customer=customer, total=total, status="created")
        self.orders[order.id] = order
        return order

    def pay_order(self, order_id: str) -> Order:
        order = self.orders[order_id]
        order.status = "paid"
        return order
