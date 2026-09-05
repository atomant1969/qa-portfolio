import pytest


@pytest.fixture
def response_time_samples_ms() -> list[float]:
    return [120, 130, 125, 140, 155, 160, 180, 220, 240, 260]
