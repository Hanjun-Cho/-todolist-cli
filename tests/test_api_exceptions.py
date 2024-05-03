import json
import pytest
from tests.conftest import client

# checks that the tasks aren't being retrieved for an invalid date
def test_get_invalid_date_tasks(client):
    with pytest.raises(ValueError) as e_info:
        response = client.get('/api/get_tasks/abcd')
        assert "invalid date format" == str(e_info)

# checks that tasks are unable to be added to an invalid date
def test_add_invalid_task_to_date(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/add_task/abcd', data = {
            "Title": "task4", "Priority": "MEDIUM", "Status": 0, "Date": "abcd"             
        })
        assert "invalid date format" == str(e_info)

# checks that tasks are unable to be added to a valid date if missing title field
def test_add_task_to_date_no_title(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/add_task/2024-May-1', data = {
            "Priority": "MEDIUM", "Status": 0, "Date": "2024-May-1"             
        })
        assert "error: title not in given task data" == str(e_info)

# checks that tasks are unable to be added to a valid date if missing priority field
def test_add_task_to_date_no_priority(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/add_task/2024-May-1', data = {
            "Title": "task4", "Status": 0, "Date": "2024-May-1"             
        })
        assert "error: priority not in given task data" == str(e_info)

# checks that tasks are unable to be added to a valid date if missing status field
def test_add_task_to_date_no_status(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/add_task/2024-May-1', data = {
            "Title": "task4", "Priority": "MEDIUM", "Date": "2024-May-1"             
        })
        assert "error: status not in given task data" == str(e_info)

# checks that tasks are unable to be added to a valid date if missing date field
def test_add_task_to_date_no_date(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/add_task/2024-May-1', data = {
            "Title": "task4", "Priority": "MEDIUM", "Status": 0
        })
        assert "error: date not in given task date" == str(e_info)

# checks that tasks are disallowed from being removed from invalid dates
def test_remove_task_from_invalid_date(client):
    with pytest.raises(ValueError) as e_info:
        response = client.post('/api/remove_task/abcd/3', data = {
            "date": 'abcd', 'taskID': 3
        })
        assert "error: invalid date format" == str(e_info)

# checks that invalid tests are disallowed from being removed
def test_remove_invalid_task_from_date(client):
    with pytest.raises(Exception) as e_info:
        response = client.post('/api/remove_task/2024-May-1/4', data = {
            "date": '2024-May-1', 'taskID': 4
        })
        assert "error: invalid taskID given" == str(e_info)
