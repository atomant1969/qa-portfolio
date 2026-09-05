class OrderRepository:
    def __init__(self) -> None:
        self.records: dict[str, dict[str, object]] = {}

    def save(self, order_id: str, order: dict[str, object]) -> None:
        self.records[order_id] = order

    def get(self, order_id: str) -> dict[str, object]:
        return self.records[order_id]
