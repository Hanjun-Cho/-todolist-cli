import json
import pytest
from pytest_mock import mocker
from tests.conftest import client

def test_get_valid_date_tasks(client):
    response = client.get('/api/get_tasks/2024-May-1')
    # checks that the response went through
    assert response.status_code == 200
    # checks that the response isn't None
    assert response != None
    # checks that the response had the right fields
    assert "tasks" in json.loads(response.data)

def test_get_invalid_date_tasks(client, mocker):
    mocked_method = mocker.patch('validation.DateValidation.validate_date')
    mocked_method.side_effect = ValueError('incorrect date format')
    # calls pytest with the intention of finding an exception
    with pytest.raises(ValueError) as exc_info:
        client.get('/api/get_tasks/abcd')
    # calls that the right exception was raised
    assert "incorrect date format" in str(exc_info.value)
