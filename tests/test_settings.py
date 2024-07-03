import pytest

from fast_open_db_brasil.settings import Settings


@pytest.mark.usefixtures('_set_env')
def test_settings_from_env_file():
    settings = Settings()
    assert settings.DATABASE_URL == 'sqlite:///example.db'
