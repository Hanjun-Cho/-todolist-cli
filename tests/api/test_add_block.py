import pytest
from tests.conftest import client

def test_add_block(client):
    response = client.post('/api/2024-May-1/blocks', data={
        "Title": "block4",
        "StartTime": "10:15",
        "EndTime": "12:45",
        "Finished": 0
    })
    assert response.status_code == 200
    assert response.json["BlockID"] == 4
    assert response.json["Title"] == "block4"

def test_not_add_block_when_invalid_date(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/abcd/blocks', data={
            "Title": "block4",
            "StartTime": "10:15",
            "EndTime": "12:45",
            "Finished": 0,
        })
        assert "error: invalid date format" == str(e_info)

def test_not_add_block_when_missing_title_in_form(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/2024-May-1/blocks', data={
            "StartTime": "10:15",
            "EndTime": "12:45",
            "Finished": 0,
        })
        assert "error: title not in given task data" == str(e_info)

def test_not_add_block_when_missing_start_time_in_form(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/2024-May-1/blocks', data={
            "Title": "block4",
            "EndTime": "12:45",
            "Finished": 0,
        })
        assert "error: start time not in given task data" == str(e_info)

def test_not_add_block_when_missing_end_time_in_form(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/2024-May-1/blocks', data={
            "Title": "block4",
            "StartTime": "10:15",
            "Finished": 0,
        })
        assert "error: end time not in given task data" == str(e_info)

def test_not_add_block_when_missing_finished_time_in_form(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/2024-May-1/blocks', data={
            "Title": "block4",
            "StartTime": "10:15",
            "EndTime": "12:45"
        })
        assert "error: finished not in given task data" == str(e_info)
