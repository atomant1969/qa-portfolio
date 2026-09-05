from datetime import datetime, timezone
from typing import Annotated
from uuid import UUID, uuid4

from fastapi import Depends, FastAPI, Header, HTTPException, Query, status
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float = Field(gt=0)
    in_stock: bool


class OrderCreate(BaseModel):
    customer: str = Field(min_length=2, max_length=80)
    product_id: int
    quantity: int = Field(gt=0, le=100)


class Order(OrderCreate):
    id: UUID
    status: str
    created_at: datetime


app = FastAPI(title="QA Store API", version="1.0.0")

VALID_TOKEN = "portfolio-token"
products = {
    1: Product(id=1, name="QA Automation Toolkit", category="testing", price=99.0, in_stock=True),
    2: Product(id=2, name="Performance Test Pack", category="performance", price=149.0, in_stock=True),
    3: Product(id=3, name="Legacy Migration Checklist", category="documentation", price=29.0, in_stock=False),
}
orders: dict[UUID, Order] = {}


def require_auth(authorization: Annotated[str | None, Header()] = None) -> None:
    if authorization != f"Bearer {VALID_TOKEN}":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing token")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/auth/login", response_model=TokenResponse)
def login(payload: LoginRequest) -> TokenResponse:
    if payload.username == "qa.engineer" and payload.password == "correct-password":
        return TokenResponse(access_token=VALID_TOKEN)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


@app.get("/products", response_model=list[Product])
def list_products(
    category: str | None = None,
    in_stock: bool | None = None,
) -> list[Product]:
    result = list(products.values())
    if category is not None:
        result = [product for product in result if product.category == category]
    if in_stock is not None:
        result = [product for product in result if product.in_stock is in_stock]
    return result


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int) -> Product:
    try:
        return products[product_id]
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Product not found") from exc


@app.post("/orders", response_model=Order, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_auth)])
def create_order(payload: OrderCreate) -> Order:
    product = get_product(payload.product_id)
    if not product.in_stock:
        raise HTTPException(status_code=409, detail="Product is out of stock")

    order = Order(
        id=uuid4(),
        customer=payload.customer,
        product_id=payload.product_id,
        quantity=payload.quantity,
        status="created",
        created_at=datetime.now(timezone.utc),
    )
    orders[order.id] = order
    return order


@app.get("/orders", response_model=list[Order], dependencies=[Depends(require_auth)])
def list_orders(status_filter: Annotated[str | None, Query(alias="status")] = None) -> list[Order]:
    if status_filter is None:
        return list(orders.values())
    return [order for order in orders.values() if order.status == status_filter]


@app.get("/orders/{order_id}", response_model=Order, dependencies=[Depends(require_auth)])
def get_order(order_id: UUID) -> Order:
    try:
        return orders[order_id]
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Order not found") from exc


@app.patch("/orders/{order_id}/status", response_model=Order, dependencies=[Depends(require_auth)])
def update_order_status(order_id: UUID, new_status: str) -> Order:
    allowed = {"created", "paid", "shipped", "cancelled"}
    if new_status not in allowed:
        raise HTTPException(status_code=422, detail="Unsupported order status")

    order = get_order(order_id)
    updated = order.model_copy(update={"status": new_status})
    orders[order_id] = updated
    return updated
