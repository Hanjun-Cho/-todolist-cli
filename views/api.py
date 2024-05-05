from validation import DateValidation, TaskIDValidation, BlockIDValidation, TaskDataFormatValidation, BlockDataFormatValidation
from flask import current_app, Blueprint, request, redirect
import database as db
api = Blueprint('api', __name__, url_prefix='/api')

@api.route("/<date>/tasks/<int:task_id>", methods=['GET', 'DELETE'])
def task(date, task_id):
    DateValidation(date)
    TaskIDValidation(date, task_id)

    if request.method == 'GET':
        return db.get_task(date, task_id)
    elif request.method == 'DELETE':
        db.remove_task(task_id)
        return {'message': 'successfully removed task'}


@api.route("/<date>/blocks/<int:block_id>", methods=['GET', 'DELETE'])
def block(date, block_id):
    DateValidation(date)
    BlockIDValidation(date, block_id)

    if request.method == 'GET':
        return db.get_block(date, block_id)
    elif request.method == 'DELETE':
        db.remove_block(block_id)
        return {'message': 'successfully removed block'}

@api.route("/<date>/tasks", methods=['GET', 'POST'])
def tasks(date):
    DateValidation(date)

    if request.method == 'GET':
        return db.get_all_tasks(date)
    elif request.method == 'POST':
        task_data = request.form
        TaskDataFormatValidation(task_data)
        return db.get_task(date, db.add_task(date, task_data))

@api.route("/<date>/blocks", methods=['GET', 'POST'])
def blocks(date):
    DateValidation(date)

    if request.method == 'GET':
        return db.get_all_blocks(date)
    elif request.method == 'POST':
        block_data = request.form
        BlockDataFormatValidation(block_data)
        return db.get_block(date, db.add_block(date, block_data))

