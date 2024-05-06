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

def execute_query(query, err_message, fetch):
    try:
        cursor = current_app.db.connection.cursor()
        cursor.execute(query)
        if fetch: ret = cursor.fetchall()
        current_app.db.connection.commit()
        cursor.close()
        if fetch: return jsonify(ret)
    except Exception:
        raise Exception(f"error: {err_message}")

def add_task(date, task_data):
    query = f"""
        INSERT INTO {current_app.config['TASK_TABLE']} (Title,Priority,AccountedFor,Date)
        VALUES ('{task_data["Title"]}', '{task_data["Priority"]}', '{task_data["AccountedFor"]}', '{date}');
    """
    execute_query(query, f"couldn't add task to {date}", False)
    return execute_query("SELECT @@IDENTITY as last;", f"couldn't fetch last inserted task_id", True).json[0]["last"]

def add_block(date, block_data):
    query = f"""
        INSERT INTO {current_app.config['BLOCK_TABLE']} (Title,StartTime,EndTime,Finished,Date)
        VALUES ('{block_data["Title"]}', '{block_data["StartTime"]}', '{block_data["EndTime"]}', '{block_data["Finished"]}', '{date}');
    """
    execute_query(query, f"couldn't add block to {date}", False)
    return execute_query("SELECT @@IDENTITY as last;", f"couldn't fetch last inserted block_id", True).json[0]["last"]

def get_all_tasks(date):
    query = f"""
        SELECT * FROM {current_app.config['TASK_TABLE']}
        WHERE Date='{date}';
    """
    return execute_query(query, f"couldn't get any tasks from {date}", True)

def get_all_blocks(date):
    query = f"""
        SELECT * FROM {current_app.config['BLOCK_TABLE']}
        WHERE Date='{date}';
    """
    return execute_query(query, f"couldn't get any blocks from {date}", True)

def get_task(date, task_id):
    query = f"""
        SELECT * FROM {current_app.config['TASK_TABLE']}
        WHERE Date='{date}' AND TaskID={task_id};
    """
    return execute_query(query, f"unable to fetch task with task_id {task_id}", True).json[0]

def get_block(date, block_id):
    query = f"""
        SELECT * FROM {current_app.config['BLOCK_TABLE']}
        WHERE Date='{date}' AND BlockID={block_id};
    """
    return execute_query(query, f"unable to fetch block with block_id {block_id}", True).json[0]

def remove_task(date, task_id):
    query = f"""
        DELETE FROM {current_app.config['TASK_TABLE']}
        WHERE Date='{date}' AND TaskID={task_id};
    """
    return execute_query(query, f"unable to delete task with task_id {task_id}", False)

def remove_block(date, block_id):
    query = f"""
        DELETE FROM {current_app.config['BLOCK_TABLE']}
        WHERE Date='{date}' AND BlockID={block_id};
    """
    return execute_query(query, f"unable to delete task with block_id {block_id}", False)

def update_task(date, task_data, task_id):
    query = f"""
        UPDATE {current_app.config['TASK_TABLE']}
        SET Title='{task_data["Title"]}', Priority='{task_data["Priority"]}',
        AccountedFor='{task_data["AccountedFor"]}', Date='{task_data["Date"]}'
        WHERE TaskID='{task_id}';
    """
    return execute_query(query, f"unable to update task with task_id {task_id}", False)

def update_block(date, block_data, block_id):
    query = f"""
        UPDATE {current_app.config['BLOCK_TABLE']}
        SET Title='{block_data["Title"]}', StartTime='{block_data["StartTime"]}',
        EndTime='{block_data["EndTime"]}', Finished='{block_data["Finished"]}',
        Date='{block_data["Date"]}' WHERE BlockID='{block_id}';
    """
    return execute_query(query, f"unable to update task with block_id {block_id}", False)
