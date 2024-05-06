import pytest

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

def test_add_task(client):
    response = client.post('/api/2024-May-1/tasks', data={
        "Title": "task4",
        "Priority": "LOW",
        "AccountedFor": 0
    })
    assert response.status_code == 200
    assert response.json["TaskID"] == 4
    assert response.json["Title"] == "task4"

def test_delete_block(client):
    response = client.delete('/api/2024-May-1/blocks/1')
    assert response.status_code == 200
    assert response.json["message"] == "successfully removed block"

def test_delete_task(client):
    response = client.delete('/api/2024-May-1/tasks/3')
    assert response.status_code == 200
    assert response.json["message"] == "successfully removed task"

def test_get_block(client):
    response = client.get('/api/2024-May-1/blocks/1')
    assert response.status_code == 200
    assert response.json["BlockID"] == 1

def test_get_blocks(client):
    response = client.get('/api/2024-May-1/blocks')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_blocks_when_date_doesnt_have_tasks(client):
    response = client.get('/api/2024-May-5/blocks')
    assert response.status_code == 200
    assert len(response.json) == 0

def test_get_task(client):
    response = client.get('/api/2024-May-1/tasks/3')
    assert response.status_code == 200
    assert response.json["TaskID"] == 3

def test_get_tasks(client):
    response = client.get('/api/2024-May-1/tasks')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_tasks_when_date_doesnt_have_tasks(client):
    response = client.get('/api/2024-May-5/tasks')
    assert response.status_code == 200
    assert len(response.json) == 0

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
