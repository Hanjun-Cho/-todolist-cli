import pytest
from tests.conftest import client

def test_get_task(client):
    response = client.get('/api/2024-May-1/tasks/3')
    assert response.status_code == 200
    assert response.json["TaskID"] == 3

def test_not_get_task_when_invalid_date(client):
    with pytest.raises(ValueError) as e_info:
        response = client.get('/api/abcd/tasks/1')
        assert "error: invalid date format" == str(e_info)

def test_not_get_task_when_invalid_task_id(client):
    with pytest.raises(Exception) as e_info:
        response = client.get('/api/2024-May-1/tasks/0')
        assert "error: invalid task_id given" == str(e_info)

def test_not_get_task_when_valid_task_id_not_from_valid_date(client):
    with pytest.raises(Exception) as e_info:
        response = client.get('/api/2024-May-1/tasks/1')
        assert "error: invalid task_id given" == str(e_info)
