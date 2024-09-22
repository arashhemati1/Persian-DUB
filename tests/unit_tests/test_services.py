import pytest
from asr_service import app as asr_app

@pytest.fixture
def client():
    with asr_app.test_client() as client:
        yield client

def test_asr(client):
    rv = client.post('/asr', data={"file": open("sample.mp4", "rb")})
    assert b"ASR text output" in rv.data
