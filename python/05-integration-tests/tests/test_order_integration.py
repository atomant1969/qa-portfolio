import pytest

pytestmark = pytest.mark.integration


def test_service_persists_order_in_repository(repository, order_service):
    created = order_service.create_order("Robert Joyce", "QA Automation Toolkit")
    stored = repository.get(created["id"])

    assert stored == created
    assert stored["status"] == "created"
