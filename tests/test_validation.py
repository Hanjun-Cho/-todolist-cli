import pytest
from validation import DateValidation, TaskIDValidation, BlockIDValidation, TaskDataFormatValidation, BlockDataFormatValidation

def test_block_data_format_validation_when_not_update():
    BlockDataFormatValidation({
        "Title": "title",
        "StartTime": "0:00",
        "EndTime": "0:00",
        "Finished": 0,
    }, update=False)
    assert True

def test_block_data_format_validation_when_update():
    BlockDataFormatValidation({
        "Title": "title",
        "StartTime": "0:00",
        "EndTime": "0:00",
        "Finished": 0,
        "Date": "2024-May-1"
    }, update=True)
    assert True

def test_not_block_data_format_validation_when_missing_title():
    with pytest.raises(ValueError) as e_info:
        BlockDataFormatValidation({
            "StartTime": "0:00",
            "EndTime": "0:00",
            "Finished": 0,
        }, update=False)
        assert "error: title not in given block data" == str(e_info)

def test_not_block_data_format_validation_when_missing_start_time():
    with pytest.raises(ValueError) as e_info:
        BlockDataFormatValidation({
            "Title": "title",
            "EndTime": "0:00",
            "Finished": 0,
        }, update=False)
        assert "error: start time not in given block data" == str(e_info)

def test_not_block_data_format_validation_when_missing_end_time():
    with pytest.raises(ValueError) as e_info:
        BlockDataFormatValidation({
            "Title": "title",
            "StartTime": "0:00",
            "Finished": 0,
        }, update=False)
        assert "error: end time not in given block data" == str(e_info)

def test_not_block_data_format_validation_when_missing_finished():
    with pytest.raises(ValueError) as e_info:
        BlockDataFormatValidation({
            "Title": "title",
            "StartTime": "0:00",
            "EndTime": "0:00"
        }, update=False)
        assert "error: finished not in given block data" == str(e_info)

def test_not_block_data_format_validation_when_missing_date_and_update():
    with pytest.raises(ValueError) as e_info:
        BlockDataFormatValidation({
            "Title": "title",
            "StartTime": "0:00",
            "EndTime": "0:00",
            "Finished": 0
        }, update=True)
        assert "error: date not in given block data" == str(e_info)

def test_block_id_validation(app):
    with app.app_context():
        BlockIDValidation("2024-May-1", 1)
        assert True

def test_not_block_id_validation_when_invalid_block_id():
    with pytest.raises(Exception) as e_info:
        BlockIDValidation("2024-May-1", 0)
        assert "error: invalid block_id given" == str(e_info)

def test_not_block_id_validation_when_valid_block_id_not_in_valid_date():
    with pytest.raises(Exception) as e_info:
        BlockIDValidation("2024-May-1", 2)
        assert "error: invalid block_id given" == str(e_info)

def test_date_validation():
    DateValidation("2024-May-1")
    assert True

def test_not_date_validation_when_wrong_format():
    with pytest.raises(ValueError) as e_info:
        DateValidation("May-1-2024")
        assert "error: invalid date format" == str(e_info)

def test_task_data_format_validation_when_not_update():
    TaskDataFormatValidation({
        "Title": "title",
        "Priority": "priority",
        "AccountedFor": 0
    }, update=False)
    assert True

def test_task_data_format_validation_when_update():
    TaskDataFormatValidation({
        "Title": "title",
        "Priority": "priority",
        "AccountedFor": 0,
        "Date": "2024-May-1"
    }, update=True)
    assert True

def test_not_task_data_format_validation_when_missing_title():
    with pytest.raises(ValueError) as e_info:
        TaskDataFormatValidation({
            "Priority": "priority",
            "AccountedFor": 0,
            "Date": "2024-May-1"
        }, update=False)
        assert "error: title not in given task data" == str(e_info)

def test_not_task_data_format_validation_when_missing_priority():
    with pytest.raises(ValueError) as e_info:
        TaskDataFormatValidation({
            "Title": "title",
            "AccountedFor": 0,
            "Date": "2024-May-1"
        }, update=False)
        assert "error: priority not in given task data" == str(e_info)

def test_not_task_data_format_validation_when_missing_accounted_for():
    with pytest.raises(ValueError) as e_info:
        TaskDataFormatValidation({
            "Title": "title",
            "Priority": "priority",
            "Date": "2024-May-1"
        }, update=False)
        assert "error: accounted for not in given task data" == str(e_info)

def test_not_task_data_format_validation_when_missing_date_and_update():
    with pytest.raises(ValueError) as e_info:
        TaskDataFormatValidation({
            "Title": "title",
            "Priority": "priority",
            "AccounteFor": 0
        }, update=True)
        assert "error: date not in given task data" == str(e_info)

def test_task_id_validation(app):
    with app.app_context():
        TaskIDValidation("2024-May-1", 3) 
        assert True

def test_not_task_id_validation_when_invalid_task_id():
    with pytest.raises(Exception) as e_info:
        TaskIDValidation("2024-May-1", 0)
        assert "error: invalid task_id given" == str(e_info)

def test_not_task_id_validation_when_valid_task_id_not_in_valid_date():
    with pytest.raises(Exception) as e_info:
        TaskIDValidation("2024-May-1", 1)
        assert "error: invalid task_id given" == str(e_info)
