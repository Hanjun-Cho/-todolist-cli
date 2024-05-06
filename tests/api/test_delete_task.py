import pytest
from tests.conftest import client

def test_delete_task(client):
    response = client.delete('/api/2024-May-1/tasks/3')
    assert response.status_code == 200
    assert response.json["message"] == "successfully removed task"

def test_not_delete_task_when_invalid_date(client):
    with pytest.raises(Exception) as e_info:
        response = client.delete('/api/abcd/tasks/3')
        assert "error: invalid date format" == str(e_info)

def test_not_delete_task_when_invalid_task_id(client):
    with pytest.raises(Exception) as e_info:
        response = client.delete('/api/2024-May-1/tasks/0')
        assert "error: invalid task_id given" == str(e_info)

def test_not_delete_task_when_valid_task_id_not_in_valid_date(client):
    with pytest.raises(Exception) as e_info:
        response = client.delete('/api/2024-May-1/tasks/1')
        assert "error: invalid task_id given" == str(e_info)
