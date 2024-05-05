import pytest
from tests.conftest import client

def test_get_tasks(client):
    response = client.get('/api/2024-May-1/tasks')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_tasks_when_date_doesnt_have_tasks(client):
    response = client.get('/api/2024-May-5/tasks')
    assert response.status_code == 200
    assert len(response.json) == 0

def test_not_get_tasks_when_invalid_date(client):
    with pytest.raises(ValueError) as e_info:
        response = client.get('/api/abcd/tasks')
        assert "error: invalid date format" == str(e_info)
