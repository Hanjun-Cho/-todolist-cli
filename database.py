from flask import jsonify

def initialize_database(db, testing):
    try:
        table_name = 'tasks' if not testing else 'test_tasks'
        cursor = db.connection.cursor()
        if testing: cursor.execute("DROP TABLE IF EXISTS test_tasks;")
        sql_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                TaskID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                Title VARCHAR(100),
                Priority VARCHAR(10) NOT NULL DEFAULT 'LOW',
                Status INT NOT NULL DEFAULT 0,
                Date VARCHAR(50)
            );
        """
        cursor.execute(sql_query)
        if testing: fill_test_database(db)
        db.connection.commit()
        cursor.close()
    except Exception:
        raise Exception("error: database wasn't initialized")

def fill_test_database(db):
    try:
        cursor = db.connection.cursor()
        cursor.execute("""
            INSERT INTO test_tasks (Title,Priority,Status,Date) 
            VALUES ('task1','HIGH',0,'2024-Apr-30'),
            ('task2','MEDIUM',2,'2024-Apr-30'),
            ('task3','LOW',1,'2024-May-1');
        """)
        db.connection.commit()
        cursor.close()
    except Exception:
        raise Exception("error: wasn't able to fill test database'")

def get_tasks_from_date(db, date, testing):
    try:
        table_name = "tasks" if not testing else "test_tasks"
        cursor = db.connection.cursor()
        sql_query = f"SELECT * FROM {table_name} WHERE Date='{date}';"
        cursor.execute(sql_query)
        tasks = cursor.fetchall()
        cursor.close()
        return jsonify(tasks)
    except Exception:
        raise Exception("error: unable to fetch items")

def add_task_to_date(task, db, date, testing):
    if "Title" not in task: return { "error": "missing title field" }
    if "Priority" not in task: return { "error": "missing priority field" }
    if "Status" not in task: return { "error": "missing status field" }
    if "Date" not in task: return { "error": "missing date field" }

    try:
        table_name = "tasks" if not testing else "test_tasks"
        cursor = db.connection.cursor()
        sql_query = f"""
            INSERT INTO {table_name} (Title,Priority,Status,Date)
            VALUES ('{task["Title"]}','{task["Priority"]}',{task["Status"]},'{date}');
        """
        cursor.execute(sql_query)
        db.connection.commit()
        cursor.close()
        return {}
    except Exception:
        return { "error": "task was unable to be added to database" }

