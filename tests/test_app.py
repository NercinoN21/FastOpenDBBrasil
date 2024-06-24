from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_open_db_brasil.app import app


def test_read_root_deve_retornar_ok_e_hello_world():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello, World!'}  # Assert
