from validation import DateValidation
from flask import current_app, Blueprint
from database import get_tasks_from_date
api = Blueprint('api', __name__, url_prefix='/api')

@api.route("/get_tasks/<date>", methods=['GET'])
def get_tasks(date):
    response = DateValidation(date).validate_date()
    if "error" in response:
        return response
    return get_tasks_from_date(current_app.db, date, current_app.config['TESTING'])

@api.route("/add_task/<date>", methods=['POST'])
def add_task(date, db, testing):
    DateValidation(date).validate_date()
    form = request.form
    print(form)
    return get_tasks(date, db, current_app.config['TESTING']) 
