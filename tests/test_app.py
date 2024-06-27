from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user_deve_retornar_created_e_user_criado(client):
    user_data = {
        'username': 'test_user',
        'email': 'test@test.com',
        'password': 'passwordtest',
    }

    response = client.post('/users/', json=user_data)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'user_id': 1,
        'username': 'test_user',
        'email': 'test@test.com',
    }


def test_read_users_deve_retornar_ok_e_lista_de_user(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'user_id': 1, 'username': 'test_user', 'email': 'test@test.com'}
        ]
    }


def test_read_user_deve_retornar_ok_e_user_atualizado(client):
    user_data = {
        'username': 'test_user_updated',
        'email': 'test_updated@test.com',
        'password': 'test@test.com',
    }

    response = client.put('/users/1', json=user_data)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'user_id': 1,
        'username': 'test_user_updated',
        'email': 'test_updated@test.com',
    }


def test_update_user_deve_retornar_not_found(client):
    user_data = {
        'username': 'test_user_updated',
        'email': 'test_updated@test.com',
        'password': 'test@test.com',
    }

    response = client.put('/users/2', json=user_data)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_deve_retornar_ok_e_mensagem_de_delete(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_deve_retornar_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_banco_de_dados_deve_ser_vazio(client):
    response = client.get('/users/')

    assert response.json() == {'users': []}
