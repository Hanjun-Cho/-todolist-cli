import pytest
from tests.conftest import client

def test_update_block_title(client):
    response = client.post('/api/2024-May-1/blocks/1', data={
        "Title": "block1b",
        "StartTime": "14:20",
        "EndTime": "15:30",
        "Finished": 0,
        "Date": "2024-May-1"
    })
    assert response.status_code == 200
    assert response.json["BlockID"] == 1
    assert response.json["Title"] == "block1b"

def test_update_block_start_time(client):
    response = client.post('/api/2024-May-1/blocks/1', data={
        "Title": "block1",
        "StartTime": "15:20",
        "EndTime": "15:30",
        "Finished": 0,
        "Date": "2024-May-1"
    })
    assert response.status_code == 200
    assert response.json["BlockID"] == 1
    assert response.json["StartTime"] == "15:20"

def test_update_block_end_time(client):
    response = client.post('/api/2024-May-1/blocks/1', data={
        "Title": "block1",
        "StartTime": "14:20",
        "EndTime": "16:30",
        "Finished": 0,
        "Date": "2024-May-1"
    })
    assert response.status_code == 200
    assert response.json["BlockID"] == 1
    assert response.json["EndTime"] == "16:30"

def test_update_block_finished(client):
    response = client.post('/api/2024-May-1/blocks/1', data={
        "Title": "block1",
        "StartTime": "14:20",
        "EndTime": "15:30",
        "Finished": 1,
        "Date": "2024-May-1"
    })
    assert response.status_code == 200
    assert response.json["BlockID"] == 1
    assert response.json["Finished"] == 1

def test_update_block_date(client):
    response = client.post('/api/2024-May-1/blocks/1', data={
        "Title": "block1",
        "StartTime": "14:20",
        "EndTime": "15:30",
        "Finished": 0,
        "Date": "2024-May-3"
    })
    assert response.status_code == 200
    assert response.json["BlockID"] == 1
    assert response.json["Date"] == "2024-May-3"
