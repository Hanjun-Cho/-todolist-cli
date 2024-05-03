from flask import jsonify, current_app

# initializes the mySQL database if it doesn't already
def initialize_database():
    try:
        cursor = current_app.db.connection.cursor()
        if current_app.config['TESTING']: cursor.execute("DROP TABLE IF EXISTS test_tasks;")
        sql_query = f"""
            CREATE TABLE IF NOT EXISTS {current_app.config['TASK_TABLE']} (
                TaskID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                Title VARCHAR(100),
                Priority VARCHAR(10) NOT NULL DEFAULT 'LOW',
                Status INT NOT NULL DEFAULT 0,
                Date VARCHAR(50)
            );
        """
        cursor.execute(sql_query)
        fill_test_database()
        current_app.db.connection.commit()
        cursor.close()
    except Exception:
        raise Exception("error: database wasn't initialized")

# fills the testing database needed to run pytests
def fill_test_database():
    if not current_app.config['TESTING']: return
    try:
        cursor = current_app.db.connection.cursor()
        cursor.execute("""
            INSERT INTO test_tasks (Title,Priority,Status,Date) 
            VALUES ('task1','HIGH',0,'2024-Apr-30'),
            ('task2','MEDIUM',2,'2024-Apr-30'),
            ('task3','LOW',1,'2024-May-1');
        """)
        current_app.db.connection.commit()
        cursor.close()
    except Exception:
        raise Exception("error: wasn't able to fill test database'")

# produces all tasks as a list from the given date
def get_tasks_from_date(date):
    try:
        cursor = current_app.db.connection.cursor()
        sql_query = f"SELECT * FROM {current_app.config['TASK_TABLE']} WHERE Date='{date}';"
        cursor.execute(sql_query)
        tasks = cursor.fetchall()
        cursor.close()
        return jsonify(tasks)
    except Exception:
        raise Exception(f"error: unable to fetch tasks from {date}")

# inserts a new task given the task data on the given date
def add_task_to_date(task, date):
    try:
        cursor = current_app.db.connection.cursor()
        sql_query = f"""
            INSERT INTO {current_app.config['TASK_TABLE']} (Title,Priority,Status,Date)
            VALUES ('{task["Title"]}','{task["Priority"]}',{task["Status"]},'{date}');
        """
        cursor.execute(sql_query)
        current_app.db.connection.commit()
        cursor.close()
    except Exception:
        raise Exception(f"error: unable to add task to {date}")

# removes the task with given taskID from the given date from the database
def remove_task_from_date(taskID, date):
    try:
        cursor = current_app.db.connection.cursor()
        sql_query = f"""
            DELETE FROM {current_app.config['TASK_TABLE']} 
            WHERE TaskID={taskID} AND Date='{date}';
        """
        cursor.execute(sql_query)
        current_app.db.connection.commit()
        cursor.close()
    except Exception:
        raise Exception(f"error: could not remove task with taskID {taskID}")
