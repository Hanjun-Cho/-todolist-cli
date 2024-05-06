import pytest
from tests.conftest import client

def test_delete_block(client):
    response = client.delete('/api/2024-May-1/blocks/1')
    assert response.status_code == 200
    assert response.json["message"] == "successfully removed block"

def test_not_delete_block_when_invalid_date(client):
    with pytest.raises(Exception) as e_info:
        response = client.delete('/api/abcd/blocks/3')
        assert "error: invalid date format" == str(e_info)

def test_not_delete_block_when_invalid_task_id(client):
    with pytest.raises(Exception) as e_info:
        response = client.delete('/api/2024-May-1/tasks/0')
        assert "error: invalid task_id given" == str(e_info)

def test_not_delete_block_when_valid_block_id_not_in_valid_date(client):
    with pytest.raises(Exception) as e_info:
        response = client.delete('/api/2024-May-1/tasks/2')
        assert "error: invalid task_id given" == str(e_info)
