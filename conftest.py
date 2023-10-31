import pytest
from api import PetstoreAPI, BASE_URL


@pytest.fixture(scope="session")
def api(request: pytest.FixtureRequest):
    yield PetstoreAPI(BASE_URL)


