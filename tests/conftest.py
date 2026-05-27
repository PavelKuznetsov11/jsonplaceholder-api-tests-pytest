import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()