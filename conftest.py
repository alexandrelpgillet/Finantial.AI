import sys
import os
from fastapi.testclient import TestClient

api_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "api"))

sys.path.insert(0, api_path)


import pytest
from api.main import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
