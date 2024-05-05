import pytest
from tests.conftest import client

def test_get_blocks(client):
    response = client.get('/api/2024-May-1/blocks')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_blocks_when_date_doesnt_have_tasks(client):
    response = client.get('/api/2024-May-5/blocks')
    assert response.status_code == 200
    assert len(response.json) == 0

def test_not_blocks_tasks_when_invalid_date(client):
    with pytest.raises(ValueError) as e_info:
        response = client.get('/api/abcd/blocks')
        assert "error: invalid date format" == str(e_info)
