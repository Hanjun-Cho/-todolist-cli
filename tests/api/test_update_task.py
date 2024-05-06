import pytest
from tests.conftest import client

def test_update_task_title(client):
    response = client.post('/api/2024-May-1/tasks/3', data={
        "Title": "task3b",
        "Priority": "LOW",
        "AccountedFor": 1,
        "Date": "2024-May-1"
    })
    assert response.status_code == 200
    assert response.json["TaskID"] == 3
    assert response.json["Title"] == "task3b"

def test_update_task_priority(client):
    response = client.post('/api/2024-May-1/tasks/3', data={
        "Title": "task3",
        "Priority": "MEDIUM",
        "AccountedFor": 1,
        "Date": "2024-May-1"
    })
    assert response.status_code == 200
    assert response.json["TaskID"] == 3
    assert response.json["Priority"] == "MEDIUM"

def test_update_task_accounted_for(client):
    response = client.post('/api/2024-May-1/tasks/3', data={
        "Title": "task3",
        "Priority": "LOW",
        "AccountedFor": 0,
        "Date": "2024-May-1"
    })
    assert response.status_code == 200
    assert response.json["TaskID"] == 3
    assert response.json["AccountedFor"] == 0

def test_update_task_date(client):
    response = client.post('/api/2024-May-1/tasks/3', data={
        "Title": "task3",
        "Priority": "LOW",
        "AccountedFor": 0,
        "Date": "2024-May-3"
    })
    assert response.status_code == 200
    assert response.json["TaskID"] == 3
    assert response.json["Date"] == "2024-May-3"

def test_not_update_task_when_invalid_date(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/abcd/tasks/3', data={
            "Title": "task3",
            "Priority": "LOW",
            "AccountedFor": 0,
            "Date": "2024-May-3"
        })
        assert "error: invalid date format" in str(e_info)

def test_not_update_task_when_invalid_task_id(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/2024-May-1/tasks/0', data={
            "Title": "task3",
            "Priority": "LOW",
            "AccountedFor": 0,
            "Date": "2024-May-3"
        })
        assert "error: invalid task_id given" in str(e_info)

def test_not_update_task_when_valid_task_id_not_in_valid_date(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/2024-May-1/tasks/1', data={
            "Title": "task3",
            "Priority": "LOW",
            "AccountedFor": 0,
            "Date": "2024-May-3"
        })
        assert "error: invalid task_id given" in str(e_info)

def test_not_update_task_when_missing_title(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/2024-May-1/tasks/3', data={
            "Priority": "LOW",
            "AccountedFor": 0,
            "Date": "2024-May-3"
        })
        assert "error: title not in given task data" in str(e_info)

def test_not_update_task_when_missing_priority(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/2024-May-1/tasks/3', data={
            "Title": "task3b",
            "AccountedFor": 0,
            "Date": "2024-May-3"
        })
        assert "error: priority not in given task data" in str(e_info)

def test_not_update_task_when_missing_accounted_for(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/2024-May-1/tasks/3', data={
            "Title": "task3b",
            "Priority": "MEDIUM",
            "Date": "2024-May-3"
        })
        assert "error: accounted for not in given task data" in str(e_info)

def test_not_update_task_when_missing_date(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/2024-May-1/tasks/3', data={
            "Title": "task3b",
            "Priority": "MEDIUM",
            "AccountedFor": 0
        })
        assert "error: date not in given task data" in str(e_info)
