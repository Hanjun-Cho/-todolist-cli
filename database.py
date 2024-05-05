from flask import jsonify, current_app

# initializes the mySQL database if it doesn't already
def db_initialize_database():
    try:
        cursor = current_app.db.connection.cursor()
        if current_app.config['TESTING']: 
            cursor.execute(f"DROP TABLE IF EXISTS {current_app.config['TASK_TABLE']};")
            cursor.execute(f"DROP TABLE IF EXISTS {current_app.config['BLOCK_TABLE']};")
        db_initialize_task_database(cursor)
        db_initialize_block_database(cursor)
        cursor.close()
    except Exception:
        raise Exception("error: database wasn't initialized")

# initializes the task table into the database
def db_initialize_task_database(cursor):
    sql_query = f"""
        CREATE TABLE IF NOT EXISTS {current_app.config['TASK_TABLE']} (
            TaskID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Title VARCHAR(100),
            Priority VARCHAR(10) NOT NULL DEFAULT 'LOW',
            AccountedFor TINYINT(1) NOT NULL DEFAULT 0,
            Date VARCHAR(50)
        );
    """
    cursor.execute(sql_query)
    db_fill_test_task_database(cursor)
    current_app.db.connection.commit()

# fills the testing task database needed to run pytests
def db_fill_test_task_database(cursor):
    if not current_app.config['TESTING']: return
    try:
        cursor.execute(f"""
            INSERT INTO {current_app.config['TASK_TABLE']} 
            (Title,Priority,AccountedFor,Date) 
            VALUES 
                ('task1','HIGH',0,'2024-Apr-30'),
                ('task2','MEDIUM',0,'2024-Apr-30'),
                ('task3','LOW',1,'2024-May-1');
        """)
        current_app.db.connection.commit()
    except Exception:
        raise Exception("error: wasn't able to fill test task database'")

# initializes the block table into the database
def db_initialize_block_database(cursor):
    sql_query = f"""
        CREATE TABLE IF NOT EXISTS {current_app.config['BLOCK_TABLE']} (
            BlockID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Title VARCHAR(100),
            StartTime VARCHAR(50),
            EndTime VARCHAR(50),
            Finished TINYINT(1) NOT NULL DEFAULT 0,
            Date VARCHAR(50)
        );
    """
    cursor.execute(sql_query)
    db_fill_test_block_database(cursor)
    current_app.db.connection.commit()

# fills the testing task database needed to run pytests
def db_fill_test_block_database(cursor):
    if not current_app.config['TESTING']: return
    try:
        cursor.execute(f"""
            INSERT INTO {current_app.config['BLOCK_TABLE']} 
            (Title,StartTime,EndTime,Finished,Date) 
            VALUES 
                ('block1','14:20','15:30',0,'2024-May-1'),
                ('block2','11:30','0:15',1,'2024-May-4'),
                ('block3','6:20','8:10',1,'2024-May-1');
        """)
        current_app.db.connection.commit()
    except Exception:
        raise Exception("error: wasn't able to fill test block database'")

# produces all tasks as a list from the given date
def db_get_tasks_from_date(date):
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
def db_add_task_to_date(task, date):
    try:
        cursor = current_app.db.connection.cursor()
        sql_query = f"""
            INSERT INTO {current_app.config['TASK_TABLE']} (Title,Priority,AccountedFor,Date)
            VALUES ('{task["Title"]}','{task["Priority"]}',{task["AccountedFor"]},'{date}');
        """
        cursor.execute(sql_query)
        current_app.db.connection.commit()
        cursor.close()
    except Exception:
        raise Exception(f"error: unable to add task to {date}")

# removes the task with given task_id from the given date from the database
def db_remove_task_from_date(task_id, date):
    try:
        cursor = current_app.db.connection.cursor()
        sql_query = f"""
            DELETE FROM {current_app.config['TASK_TABLE']} 
            WHERE TaskID={task_id} AND Date='{date}';
        """
        cursor.execute(sql_query)
        current_app.db.connection.commit()
        cursor.close()
    except Exception:
        raise Exception(f"error: could not remove task with taskID {taskID}")

# renames the task title with the given task_id
# from the database into new_title
def db_rename_task(task_id, new_title):
    try:
        cursor = current_app.db.connection.cursor()
        sql_query = f"""
            UPDATE {current_app.config["TASK_TABLE"]} 
            SET Title='{new_title}' WHERE TaskID={task_id};
        """
        cursor.execute(sql_query)
        current_app.db.connection.commit()
        cursor.close()
    except Exception:
        raise Exception(f"error: could not rename task with taskID {taskID}")
