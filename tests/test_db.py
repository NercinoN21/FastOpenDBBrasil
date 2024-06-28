from sqlalchemy import select

from fast_open_db_brasil.models import User


def test_create_user_deve_retornar_created_e_user_criado(session):
    user = User(username='nercino21', email='nerc@ino.com', password='123456')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).filter(User.username == 'nercino21'))

    assert result.id == 1
    assert result.username == 'nercino21'
    assert result.email == 'nerc@ino.com'
    assert result.password == '123456'
