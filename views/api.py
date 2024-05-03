from validation import DateValidation, TaskDataFormatValidation, TaskIDValidation
from flask import current_app, Blueprint, request, redirect
from database import get_tasks_from_date, add_task_to_date, remove_task_from_date
api = Blueprint('api', __name__, url_prefix='/api')

# route which produces all tasks from the given date
@api.route("/get_tasks/<date>", methods=['GET'])
def get_tasks(date):
    DateValidation(date)
    return get_tasks_from_date(date)

# route which adds a task to the given date based
# on a POSTed request form
@api.route("/add_task/<date>", methods=['POST'])
def add_task(date):
    DateValidation(date)
    TaskDataFormatValidation(request.form)
    add_task_to_date(request.form, date)
    return get_tasks_from_date(date)

# route which removes the task with the given taskID
# from the given date
@api.route("/remove_task/<date>/<int:taskID>", methods=['POST'])
def remove_task(date, taskID):
    DateValidation(date)
    TaskIDValidation(taskID)
    remove_task_from_date(taskID, date)
    return get_tasks_from_date(date)
