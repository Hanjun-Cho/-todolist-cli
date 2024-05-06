from datetime import datetime
from flask import redirect, url_for, current_app

class DateValidation:
    def __init__(self, date):
        try: dt = datetime.strptime(date, '%Y-%b-%d')
        except ValueError: raise ValueError("error: invalid date format given")

class TaskDataFormatValidation:
    def __init__(self, task, update):
        if "Title" not in task: raise ValueError("error: title not in given task data")
        if "Priority" not in task: raise ValueError("error: priority not in given task data")
        if "AccountedFor" not in task: raise ValueError("error: accounted for not in given task data")
        if update:
            if "Date" not in task: raise ValueError("error: date not in given task data")

class BlockDataFormatValidation:
    def __init__(self, block, update):
        if "Title" not in block: raise ValueError("error: title not in given block data")
        if "StartTime" not in block: raise ValueError("error: start time not in given block data")
        if "EndTime" not in block: raise ValueError("error: end time not in given block data")
        if "Finished" not in block: raise ValueError("error: finished not in given block data")
        if update:
            if "Date" not in block: raise ValueError("error: date not in given block data")

class TaskIDValidation:
    def __init__(self, date, task_id):
        try:
            cursor = current_app.db.connection.cursor()
            sql_query = f"""
                SELECT * FROM {current_app.config['TASK_TABLE']} WHERE
                TaskID={task_id} AND Date='{date}';
            """
            cursor.execute(sql_query)
            cursor.close()
        except Exception:
            raise Exception("error: invalid task_id given")

class BlockIDValidation:
    def __init__(self, date, block_id):
        try:
            cursor = current_app.db.connection.cursor()
            sql_query = f"""
                SELECT * FROM {current_app.config['BLOCK_TABLE']} WHERE
                BlockID={block_id} AND Date='{date}';
            """
            cursor.execute(sql_query)
            cursor.close()
        except Exception:
            raise Exception("error: invalid block_id given")

