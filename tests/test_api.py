import json
import pytest
from tests.conftest import client

# checks that the tasks are being retrieved for a valid date
def test_get_valid_date_tasks(client):
    response = client.get('/api/get_tasks/2024-May-1')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["Title"] == "task3"

# checks that tasks are able to be added onto a 
# valid date with valid form data
def test_add_valid_task_to_date(client):
    response = client.post('/api/add_task/2024-May-1', data = {
        "Title": "task4", "Priority": "MEDIUM", "AccountedFor": 0, "Date": "2024-May-1"             
    })
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[1]["Title"] == "task4"

# checks that a valid taskID from the correct date is 
# removed correctly from the databse
def test_remove_valid_task_to_date(client):
    response = client.get('/api/remove_task/2024-May-1/3')
    assert response.status_code == 200
    assert len(response.json) == 0

# checks that a valid task with the given taskID is
# renamed correctly according to new_title in database
def test_rename_valid_task_to_date(client):
    response = client.post('/api/rename_task/2024-May-1/3', data = {
        "new_title": "new task3"
    })
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["Title"] == "new task3"
