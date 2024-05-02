import json
import pytest
from pytest_mock import mocker
from tests.conftest import client
from views.api import get_tasks

def test_get_valid_date_tasks(client):
    response = client.get('/api/get_tasks/2024-May-1')
    # checks that the response went through
    assert response.status_code == 200
    # checks that the response is not None
    assert response != None
    # checks that the response matches test database
    assert len(response.json) == 1
    # checks that the response is correct
    assert response.json[0]["Title"] == "task3"

def test_get_invalid_date_tasks(client):
    response = client.get('/api/get_tasks/abcd')
    # checks that the response went through
    assert response.status_code == 200
    # checks that the date produced an error result
    assert "error" in response.json
