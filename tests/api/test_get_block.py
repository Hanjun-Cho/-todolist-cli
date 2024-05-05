import pytest
import pytest
from tests.conftest import client

def test_get_block(client):
    response = client.get('/api/2024-May-1/blocks/1')
    assert response.status_code == 200
    assert response.json["BlockID"] == 1

def test_not_get_block_when_invalid_date(client):
    with pytest.raises(ValueError) as e_info:
        response = client.get('/api/abcd/blocks/1')
        assert "error: invalid date format" == str(e_info)

def test_not_get_block_when_invalid_task_id(client):
    with pytest.raises(Exception) as e_info:
        response = client.get('/api/2024-May-1/blocks/0')
        assert "error: invalid task_id given" == str(e_info)

def test_not_get_block_when_valid_block_id_not_from_valid_date(client):
    with pytest.raises(Exception) as e_info:
        response = client.get('/api/2024-May-1/blocks/2')
        assert "error: invalid task_id given" == str(e_info)

