import pytest
from tests.conftest import client

def test_add_task(client):
    response = client.post('/api/2024-May-1/tasks', data={
        "Title": "task4",
        "Priority": "LOW",
        "AccountedFor": 0
    })
    assert response.status_code == 200
    assert response.json["TaskID"] == 4
    assert response.json["Title"] == "task4"

def test_not_add_task_when_invalid_date(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/abcd/tasks', data={
            "Title": "task4",
            "Priority": "LOW",
            "AccountedFor": 0,
        })
        assert "error: invalid date format" == str(e_info)

def test_not_add_task_when_missing_title_in_form(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/2024-May-1/tasks', data={
            "Priority": "LOW",
            "AccountedFor": 0
        })
        assert "error: title not in given task data" == str(e_info)

def test_not_add_task_when_missing_priority_in_form(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/2024-May-1/tasks', data={
            "Title": "task4",
            "AccountedFor": 0
        })
        assert "error: priority not in given task data" == str(e_info)

def test_not_add_task_when_missing_accounted_for_in_form(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/2024-May-1/tasks', data={
            "Title": "task4",
            "Priority": "LOW"
        })
        assert "error: accounted for not in given task data" == str(e_info)

