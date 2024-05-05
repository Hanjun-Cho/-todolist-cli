from flask import Flask, request
from flask_mysqldb import MySQL
from database import db_initialize_database
import secret

def create_app():
    return init_app(testing=False)

def create_testing_app():
    return init_app(testing=True)

# creates flask application and sets up database configurations
def init_app(testing):
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = secret.MYSQL_HOST
    app.config['MYSQL_USER'] = secret.MYSQL_USER
    app.config['MYSQL_PASSWORD'] = secret.MYSQL_PASSWORD
    app.config['MYSQL_DB'] = secret.MYSQL_DB
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    app.config['TESTING'] = testing
    app.config['TASK_TABLE'] = "tasks" if not testing else "test_tasks"
    app.config['BLOCK_TABLE'] = "blocks" if not testing else "test_blocks"
    db = MySQL(app)
    app.db = db
    with app.app_context():
        db_initialize_database()
        from views.api import api
        app.register_blueprint(api)
    return app
