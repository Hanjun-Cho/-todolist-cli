from validation import DateValidation
from flask import current_app, Blueprint, request, redirect
from database import get_tasks_from_date, add_task_to_date
api = Blueprint('api', __name__, url_prefix='/api')

@api.route("/get_tasks/<date>", methods=['GET'])
def get_tasks(date):
    response = DateValidation(date).validate_date()
    if "error" in response: return response
    return get_tasks_from_date(current_app.db, date, current_app.config['TESTING'])

@api.route("/add_task/<date>", methods=['POST'])
def add_task(date):
    validation_response = DateValidation(date).validate_date()
    if "error" in validation_response: return validation_response
    insertion_response = add_task_to_date(request.form, current_app.db, date, current_app.config['TESTING'])
    if "error" in insertion_response: return insertion_response
    return redirect(f'/get_tasks/{date}')
