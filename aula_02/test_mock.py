import pytest
import requests
from unittest.mock import MagicMock

@pytest.fixture
def mock_response():
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200
    mock.json.return_value  = {"message":"Sucess"}
    return mock

def test_api_call_with_mock1(mock_response):
    response = mock_response
    assert response.status_code == 200
    assert response.json() == {"message":"Sucess"}
    