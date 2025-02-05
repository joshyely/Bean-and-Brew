import pytest
import os
from dotenv import load_dotenv

from ...beanandbrew.config import settings

def test_settings():
    load_dotenv()
    for key in [key for key, _ in settings.model_fields.items()]:
        env_var = os.environ[key]
        settings_field = str( getattr(settings, key) )
        assert env_var == settings_field
