import json
from pathlib import Path

import pytest
from jsonschema import validate


pytestmark = pytest.mark.products


def test_list_products_returns_available_catalog(api_client):
    response = api_client.list_products()

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_list_products_can_filter_by_category(api_client):
    response = api_client.list_products(category="performance")

    assert response.status_code == 200
    assert [product["name"] for product in response.json()] == ["Performance Test Pack"]


def test_list_products_can_filter_by_stock_status(api_client):
    response = api_client.list_products(in_stock=False)

    assert response.status_code == 200
    assert [product["id"] for product in response.json()] == [3]


def test_unknown_product_returns_404(api_client):
    response = api_client.get_product(999)

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


@pytest.mark.schema
def test_product_response_matches_schema(api_client):
    schema_path = Path(__file__).parent / "schemas" / "product.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    response = api_client.get_product(1)

    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)
