import pytest
from fastapi.testclient import TestClient

from fast_open_db_brasil.app import app


@pytest.fixture()
def client():
    return TestClient(app)
