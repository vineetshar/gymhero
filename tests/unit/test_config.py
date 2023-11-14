import os

from gymhero.config import settings
import dotenv

dotenv.load_dotenv(".env.example")


def test_properly_read_config():
    for key in [key for key, _ in settings.model_fields.items()]:
        assert str(getattr(settings, key)) == os.environ[key]


def test_can_build_postgres_url():
    assert (
        f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        == "postgresql://gymhero:p4ssw0rd@localhost:5432/workout"
    )