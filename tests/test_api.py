import json
import pytest
from tests.conftest import client

# checks that the tasks are being retrieved for a valid date
def test_get_valid_date_tasks(client):
    response = client.get('/api/get_tasks/2024-May-1')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["Title"] == "task3"

# checks that the tasks aren't being retrieved for an invalid date
def test_get_invalid_date_tasks(client):
    response = client.get('/api/get_tasks/abcd')
    assert response.status_code == 200
    assert "error" in response.json

# checks that tasks are able to be added onto a valid date with valid form data
def test_add_valid_task_to_date(client):
    response = client.post('/api/add_task/2024-May-1', data = {
        "Title": "task4", "Priority": "MEDIUM", "Status": 0, "Date": "2024-May-1"             
    })
    assert response.status_code == 302

# checks that tasks are unable to be added to an invalid date
def test_add_invalid_task_to_date(client):
    response = client.post('/api/add_task/abcd', data = {
        "Title": "task4", "Priority": "MEDIUM", "Status": 0, "Date": "abcd"             
    })
    assert response.status_code == 200
    assert "error" in response.json

# checks that tasks are unable to be added to a valid date if missing title field
def test_add_task_to_date_no_title(client):
    response = client.post('/api/add_task/2024-May-1', data = {
        "Priority": "MEDIUM", "Status": 0, "Date": "2024-May-1"             
    })
    assert response.status_code == 200
    assert "error" in response.json
    assert response.json["error"] == "missing title field"

# checks that tasks are unable to be added to a valid date if missing priority field
def test_add_task_to_date_no_priority(client):
    response = client.post('/api/add_task/2024-May-1', data = {
        "Title": "task4", "Status": 0, "Date": "2024-May-1"             
    })
    assert response.status_code == 200
    assert "error" in response.json
    assert response.json["error"] == "missing priority field"

# checks that tasks are unable to be added to a valid date if missing status field
def test_add_task_to_date_no_status(client):
    response = client.post('/api/add_task/2024-May-1', data = {
        "Title": "task4", "Priority": "MEDIUM", "Date": "2024-May-1"             
    })
    assert response.status_code == 200
    assert "error" in response.json
    assert response.json["error"] == "missing status field"

# checks that tasks are unable to be added to a valid date if missing date field
def test_add_task_to_date_no_date(client):
    response = client.post('/api/add_task/2024-May-1', data = {
        "Title": "task4", "Priority": "MEDIUM", "Status": 0
    })
    assert response.status_code == 200
    assert "error" in response.json
    assert response.json["error"] == "missing date field"
